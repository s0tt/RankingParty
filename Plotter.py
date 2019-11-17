from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random as rand
from tinydb import TinyDB, Query
from config import Drinks, plotterConfig, teamConfig
import datetime
import math
from DB import DBHandler, Query

class Plotter():

    def __init__(self):
        ## disable caching because real time values are needed
        TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}
        self.DBHandler = DBHandler()

        ### init lists
        self.drinkCnt = [0] * teamConfig["numTeams"]
        self.bufferArray = [0] * teamConfig["numTeams"]
        self.bufferArrayOld = [0] * teamConfig["numTeams"]
        self.bufferListList = [0] * teamConfig["numTeams"]
        self.teamTextList = [0] * teamConfig["numTeams"]
        for i in range(0, teamConfig["numTeams"]):
            self.bufferListList[i] = [0]

    def plotFigure(self):
        fig, ax = plt.subplots(figsize=plotterConfig["figSize"])
        return fig, ax

    def plotHBar(self, axis):
        rectsHBar = axis.barh(teamConfig["teamNames"], self.drinkCnt,  height=np.full(teamConfig["numTeams"], 
                                plotterConfig["barHeight"]), color= teamConfig["teamColors"])

        for i in range(0, teamConfig["numTeams"]):
            self.teamTextList[i] = axis.text(i, 0, 0, ha='left', size=14)

        return rectsHBar

    def readDB(self):
        for teamNr in range(0, teamConfig["numTeams"]):
            query = Query()
            queryExpression = (query.team == teamNr)
            response = self.DBHandler.read(queryExpression)
            self.bufferArray[teamNr] = len(response)
        print("Updated DrinkCnt from DB at", datetime.datetime.now(), "Val: ", self.bufferArray)


    def animateHBarFunc(self, ticks, rects):
        if (ticks*plotterConfig["animIntervall"]) % plotterConfig["dbIntervall"] == 0:
            self.readDB()

        #update bar drink Cnt
        self.timeBufferManager()

        for rect, yi in zip(rects, self.drinkCnt):
            #print("Rect: ", rect, "DrinkNr: ", yi)
            rect.set_width(yi)
        #line.set_data(x, data[i])
        #ax.clear()
        for i in range(0, teamConfig["numTeams"]):
            self.teamTextList[i].set_position((self.drinkCnt[i], i))
            self.teamTextList[i].set_text(str(math.trunc(self.drinkCnt[i])))
        #val1 = ax.text(drinkCnt[1],  1,     drinkCnt[1],           ha='left')   
        plt.xlim(0, max(self.drinkCnt)+plotterConfig["xAxisLeadOffset"])
        #ax.set_xlim(auto=True)
        #print("Animate Fnc, I: ", ticks)
        #print("DrinkCt",drinkCnt) 
        
        return rects


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