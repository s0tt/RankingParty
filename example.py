from matplotlib import pyplot as plt
from matplotlib import animation
import numpy as np
import random as rand
from tinydb import TinyDB
from tinydb import Query
import threading
import PySimpleGUI as sg
from config import Drinks
import datetime
import math
from DB import DBHandler, Query


##config
x = ["Team BLAU","Team ROT", "Team GRÜN", "Team GELB"]
animIntervall = 50 #Intervall in milli seconds [ms] < as dbIntervall, % dbIntervall shall be 0
dbIntervall = 5000 #Intervall in milli seconds [ms]

 #In percent [%] of DB read out speed
 # 1 means vaues will take the whole time period dbIntervall
 # 0 means values will be directly displayed on readout
 # 10 means values that where read at time X will be fully written into the bar at time X+(10*dbIntervall)
displayTime = 0.4

#display speed 
# 1 means equally spaced displayes
displaySpeed = 1

roundPrecision = 1/100000

numTeams = 4

### init lists
drinkCnt = [0] * numTeams
bufferArray = [0] * numTeams
bufferArrayOld = [0] * numTeams
bufferListList = [0] * numTeams
teamTextList = [0] * numTeams
for i in range(0, numTeams):
    bufferListList[i] = [0]
print(bufferListList)

maxOffset = 5

TinyDB.DEFAULT_TABLE_KWARGS = {'cache_size': 0}

query = Query()

#colors
colors = dict(zip(
    ['BLAU', 'ROT', 'GRÜN', 'GELB'],
    ['#035efc','#fc2803', '#03fc77', '#fce703']
))

col = ['#035efc','#fc2803', '#03fc77', '#fce703']


DBHandler = DBHandler()

#data = np.column_stack([np.linspace(0, yi, interval) for yi in y])
#print(data)
#plt.barh()
fig, ax = plt.subplots(figsize=(15, 8))
plt.autoscale(True)

rects = ax.barh(x, np.zeros(numTeams), np.full(numTeams, 0.5), color= col)
#rects = plt.barh(x, drinkCnt, color='c')
#line, = plt.plot(x, data[0], color='r')
#plt.ylim(0, max(drinkCnt))

#setup text
#for i, (value, name) in enumerate(zip(dff['value'], dff['name'])):
#text1 = ax.text(1, 0,     "ROT",            ha='right')  # Tokyo: name
for i in range(0, numTeams):
    teamTextList[i] = ax.text(i, 0, 0, ha='left', size=14)   # 38194.2: value

print(teamTextList)

def plotDrinksCircle():
    drinkSum = []
    drinkNames = []
    for Drink in Drinks:
        DrinkQuery = Query()
        ret = DBHandler.read(DrinkQuery.type == Drink.value)
        if len(ret) > 0:
            drinkSum.append(len(ret))
            drinkNames.append(Drink.name)
    fig, ax = plt.subplots(figsize=(15, 8))
    wedges, text  = ax.pie(drinkSum, wedgeprops=dict(width=0.5))

    #label
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
    kw = dict(arrowprops=dict(arrowstyle="-"),
          bbox=bbox_props, zorder=0, va="center")

    for i, p in enumerate(wedges):
        ang = (p.theta2 - p.theta1)/2. + p.theta1
        y = np.sin(np.deg2rad(ang))
        x = np.cos(np.deg2rad(ang))
        horizontalalignment = {-1: "right", 1: "left"}[int(np.sign(x))]
        connectionstyle = "angle,angleA=0,angleB={}".format(ang)
        kw["arrowprops"].update({"connectionstyle": connectionstyle})
        ax.annotate(drinkNames[i], xy=(x, y), xytext=(1.35*np.sign(x), 1.4*y),
                horizontalalignment=horizontalalignment, **kw)

    plt.show()
      
def plotTimeSeries():
    allData = DBHandler.readAll()
    print(allData)

def addArrays(a, b):
    if len(a) < len(b):
        c = b.copy()
        c[:len(a)] += a
    else:
        c = a.copy()
        c[:len(b)] += b
    return c

def readPipe(msCnt):
    # return [rand.randint(1,10), rand.randint(1,10), rand.randint(1,10), rand.randint(1,10)]
    db = TinyDB('db.json')
    for teamNr in range(0, numTeams):
        bufferArray[teamNr] = len(db.search(query.team == teamNr))
    print("Updated DrinkCnt from DB at", datetime.datetime.now())
    #print("New Buffer: ", bufferArray)
    db.close()

def timeBufferManager():
    global drinkCnt
    #rtnArray = []
    
    for i in range(0, numTeams):
        bufferArrayDiffTeam = bufferArray[i] - bufferArrayOld[i]
        teamBufferList = bufferListList[i]

        #check for updated values       
        if bufferArrayDiffTeam != 0:
            nrUnits = (displayTime*(dbIntervall/animIntervall))
            nrUnitsRounded = round(nrUnits)
            eqSpacedValues = bufferArrayDiffTeam/(nrUnitsRounded)
            
            spacedValues = np.linspace(eqSpacedValues,eqSpacedValues, num=(nrUnitsRounded))
            #print("Spaced Vals: ", spacedValues)
            teamBufferList = addArrays(teamBufferList, spacedValues)
            #update comparison buffer
            bufferArrayOld[i] = bufferArray[i]
        
        # if bufferList is not empty values for future steps upcoming
        if len(teamBufferList) != 0:
            #print("TeamBufferList:", teamBufferList)
            drinkCnt[i] += teamBufferList[0]

             ##smooth out counter with rounding
            if (abs(drinkCnt[i]- round(drinkCnt[i]))) < roundPrecision:
                drinkCnt[i] = round(drinkCnt[i])


            #print("drinkCnt", drinkCnt)
            teamBufferList = np.delete(teamBufferList, 0)
        
        bufferListList[i] = teamBufferList
     
def animate(ticks):
    if (ticks*animIntervall) % dbIntervall == 0:
        readPipe(ticks)

    timeBufferManager()

    for rect, yi in zip(rects, drinkCnt):
        #print("Rect: ", rect, "DrinkNr: ", yi)
        rect.set_width(yi)
    #line.set_data(x, data[i])
    #ax.clear()
    for i in range(0, numTeams):
        teamTextList[i].set_position((drinkCnt[i], i))
        teamTextList[i].set_text(str(math.trunc(drinkCnt[i])))
    #val1 = ax.text(drinkCnt[1],  1,     drinkCnt[1],           ha='left')   
    plt.xlim(0, max(drinkCnt)+maxOffset)
    #ax.set_xlim(auto=True)
    #print("Animate Fnc, I: ", ticks)
    #print("DrinkCt",drinkCnt)
    
    return rects

def drawFig(fig):
    anim = animation.FuncAnimation(fig, animate, interval=animIntervall, repeat=False, blit=False) ##interval in ms
    plt.show()
    return 0


drawFig(fig)

plotDrinksCircle()
#plotTimeSeries()
#db.close()
print("Test")