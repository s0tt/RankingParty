import matplotlib
matplotlib.use('Qt5Agg')   # generate postscript output by default
from matplotlib import pyplot as plt
from matplotlib import animation, ticker
import numpy as np
import random as rand
from tinydb import TinyDB, Query
from config import Drinks, plotterConfig, teamConfig, drinkPriceMapping
import datetime
import math
from DB import DBHandler, Query

class Plotter():

    def __init__(self):
        ## disable caching because real time values are needed
        TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}
        self.DBHandler = DBHandler()

        ### special vars
        self.isSpecialActive = False
        self.teamMultipliers = [0] * teamConfig["numTeams"]

        ### init lists
        self.drinkCnt = [0] * teamConfig["numTeams"]
        self.bufferArray = [0] * teamConfig["numTeams"]
        self.bufferArrayOld = [0] * teamConfig["numTeams"]
        self.bufferListList = [0] * teamConfig["numTeams"]
        self.teamPointsTextList = [0] * teamConfig["numTeams"]
        self.teamNameTextList = [0] * teamConfig["numTeams"]
        self.dbUpdateCnt = 0
        for i in range(0, teamConfig["numTeams"]):
            self.bufferListList[i] = [0]

    def plotFigure(self):
        fig, ax = plt.subplots(figsize=plotterConfig["figSize"])
        return fig, ax

    def plotHBar(self, axis):
        rectsHBar = axis.barh(teamConfig["teamNames"], self.drinkCnt,  height=np.full(teamConfig["numTeams"], 
                                plotterConfig["barHeight"]), color= teamConfig["teamColors"], )

        #team moving point counter text
        for i in range(0, teamConfig["numTeams"]):
            self.teamPointsTextList[i] = axis.text(i, 0, 0, ha='left', size=16)

        #team moving team name text
        for i in range(0, teamConfig["numTeams"]):
            self.teamNameTextList[i] = axis.text(i, 0, teamConfig["teamNames"][i], ha='right', size=18)

        ### advanced styling
        #custom borders
        plt.subplots_adjust(top=0.75,bottom=0.055,left=0.04,right=0.95,)

        axis.text(0, 1.06, 'Teampunkte', transform=axis.transAxes, size=16, color='#777777')
        axis.xaxis.set_major_formatter(ticker.StrMethodFormatter('{x:,.0f}'))
        axis.xaxis.set_ticks_position('top')
        axis.tick_params(axis='x', colors='#777777', labelsize=16)
        axis.set_yticks([])
        axis.margins(0, 0.01)
        axis.grid(which='major', axis='x', linestyle='-')
        axis.set_axisbelow(True)
        axis.text(0, 1.12, 'Ranking Party @JC Salmendingen',
            transform=axis.transAxes, size=24, weight=600, ha='left')

        axis.text(2, 0, 'by @Stefan Ott', transform=axis.transAxes, ha='right',
            color='#777777', bbox=dict(facecolor='white', alpha=0.8, edgecolor='white'))
        return rectsHBar

    def readDB(self):
        for teamNr in range(0, teamConfig["numTeams"]):
            query = Query()
            queryExpression = (query.team == teamNr)
            response = self.DBHandler.read(queryExpression)
            self.bufferArray[teamNr] = self.calcTeamPoints(response)
        print("Updated DrinkCnt from DB at", datetime.datetime.now(), "Val: ", self.bufferArray)

    def calcTeamPoints(self, teamDrinkHistory):
        teamPoints = 0
        for drink in teamDrinkHistory:
            #convert DB drink type to enum type
            #drinkType = Drinks(drink["type"])
            #teamPoints += drinkPriceMapping[drinkType.name]/plotterConfig["pointsScaleFactor"]
            teamPoints += drink["pts"]/plotterConfig["pointsScaleFactor"]
        return teamPoints

    def animateHBarFunc(self, ticks, rects):
        #print(((ticks*plotterConfig["animIntervall"])-(self.dbUpdateCnt*plotterConfig["dbIntervall"])) )
        if ((ticks*plotterConfig["animIntervall"])-(self.dbUpdateCnt*plotterConfig["dbIntervall"])) >= plotterConfig["dbIntervall"]:
            self.readDB()
            #also execute check for specials und dbRead
            self.executeSpecials()
            self.dbUpdateCnt += 1

        #update bar drink Cnt
        self.timeBufferManager()

        for rect, yi in zip(rects, self.drinkCnt):
            #print("Rect: ", rect, "DrinkNr: ", yi)
            rect.set_width(yi)
        #line.set_data(x, data[i])
        #ax.clear()
        for i in range(0, teamConfig["numTeams"]):
            self.teamPointsTextList[i].set_position((self.drinkCnt[i]+1, i))
            self.teamPointsTextList[i].set_text(str(math.trunc(self.drinkCnt[i])))
            self.teamNameTextList[i].set_position((self.drinkCnt[i]-1, i))
        #val1 = ax.text(drinkCnt[1],  1,     drinkCnt[1],           ha='left')   
        plt.xlim(0, max(self.drinkCnt)+plotterConfig["xAxisLeadOffset"])
        #ax.set_xlim(auto=True)
        #print("Animate Fnc, I: ", ticks, "at ", datetime.datetime.now())
        #print("DrinkCt",drinkCnt) 
        


        return rects

    def executeSpecials(self):
        response = self.DBHandler.readById(1)
        if response["isActive"] != 0:
            #special got triggered
            if self.isSpecialActive is False:
                print("[Special] Special multiplier got activated!")
                self.isSpecialActive = True
                self.teamMultipliers[0] = response["boost_red"]
                self.teamMultipliers[1] = response["boost_green"]
                self.teamMultipliers[2] = response["boost_blue"]
                print("[Special] Team boosts applied")
            #special still active & running
        else:
            self.isSpecialActive = False
            print("[Special] Special multiplier deactivated!")
            self.teamMultipliers = [0] * len(self.teamMultipliers)
            print("[Special] Team boosts deactivated")



    def timeBufferManager(self):   
        for i in range(0, teamConfig["numTeams"]):
            #calculate diff since last read
            bufferArrayDiffTeam = self.bufferArray[i] - self.bufferArrayOld[i]
            teamBufferList = self.bufferListList[i]

            #check for updated values       
            if bufferArrayDiffTeam != 0:
                #determine number of bins for displaying
                nrUnits = (plotterConfig["displayTime"]*(plotterConfig["dbIntervall"]/plotterConfig["animIntervall"]))
                #round to full number because of discret update mechanism
                nrUnitsRounded = round(nrUnits)
                #determine update value for each team 
                eqSpacedValues = bufferArrayDiffTeam/(nrUnitsRounded)
                
                # space values equally over number of units
                spacedValues = np.linspace(eqSpacedValues,eqSpacedValues, num=(nrUnitsRounded))
                
                # add bins to exisiting list of bins
                teamBufferList = self.addArrays(teamBufferList, spacedValues)

                #update comparison buffer
                self.bufferArrayOld[i] = self.bufferArray[i]
            
            # if bufferList is not empty values for future steps upcoming and drink counter update is needed
            if len(teamBufferList) != 0:
                #print("TeamBufferList:", teamBufferList)
                self.drinkCnt[i] += teamBufferList[0]

                #smooth out counter by rounding values
                #due to discret adding of float values slight offsets are created
                #e.g. drinkCnt should be 15 but is 14.99999998 --> will be displayed wrong
                #Solution: if drinkCnt is close enough to next INT then round it (precision determined by roundPrecision factor)
                if (abs(self.drinkCnt[i]- round(self.drinkCnt[i]))) < plotterConfig["roundPrecision"]:
                    self.drinkCnt[i] = round(self.drinkCnt[i])


                #print("drinkCnt", drinkCnt)
                teamBufferList = np.delete(teamBufferList, 0)
            
            self.bufferListList[i] = teamBufferList

    ### function to add 2 arrays of all sizes
    # on uneven array length it fills up with 0
    def addArrays(self, a, b):
        if len(a) < len(b):
            c = b.copy()
            c[:len(a)] += a
        else:
            c = a.copy()
            c[:len(b)] += b
        return c