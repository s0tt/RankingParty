from enum import Enum

class Drinks(Enum):
    WODKA_PUR = 0
    WODKA_ORANGE = 1
    WODKA_BULL = 2
    WODKA_BRAUSE = 3

    ####
    BACARDI_PUR = 10
    BACARDI_ORANGE = 11
    BACARDI_COLA = 12

    ####
    BEER_HALBE = 20
    BEER_WEIZEN = 21
    BEER_PILS = 22
    BEER_STIEFEL = 23
    BEER_MASS = 24
    BEER_RADLER = 25

    ###
    SHOT_FICKEN = 30
    SHOT_BERLINER_LUFT = 31
    SHOT_PFEFFI = 32
    SHOT_KLOPFER = 33


    ###
    GIN_TONIC = 40


######## Plotter config values ########
plotterConfig = {
    "dbPath": "db.json",
    "animIntervall":    50,    #speed the real time graph update function is called in [ms]
    "dbIntervall":      5000,    #speed the DB is pulled for new data, Intervall in milli seconds [ms]
    
    #In percent [%] of DB read out speed
    # 1 means vaues will take the whole time period dbIntervall
    # 0 means values will be directly displayed on readout
    # 10 means values that where read at time X will be fully written into the bar at time X+(10*dbIntervall)
    "displayTime":      1.5,
    "displaySpeed":     1,          #display speed of updated values, 1 means equally spaced display times
    "roundPrecision":   1/100000,   #rounding precision to handle absolut float display issues
    "xAxisLeadOffset":  10,         #offset on the x axis in front of the highest bar to the end of the plot
    "figSize":          (15,8),     #size of the figure the graphs are plotted into
    "barHeight":        0.5,        #height of the bars
    }

teamConfig = {
    "numTeams":         4,          #number of playing teams, currently only 4 players are supported due to GUI limitations
    "teamColors": ['#035efc','#fc2803', '#03fc77', '#fce703'], #bar colors for the teams
    "teamNames": ["Team BLUE","Team RED", "Team GREEN", "Team YELLOW"],  #team names used for plots

}