from enum import Enum

class Drinks(Enum):
    WODKA_PUR = 0
    WODKA_ORANGE = 1
    WODKA_BULL = 2
    WODKA_UBOOT = 3

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
    SHOT_WODKA_BRAUSE = 34


    ###
    GIN_TONIC = 40

    ### Wine
    WINE_SEKT = 50
    WINE_HUGO = 51
    WINE_SCHORLE = 52
    WINE_FLASCHE = 53

    ## Captain
    CAPTAIN_COLA = 60

    # Non-Alcoholic
    NOALC_WASSER = 70
    NOALC_COLA = 71
    NOALC_FANTA = 72
    NOALC_BULL = 73
    NOALC_TONIC = 74

    #Special
    SPECIAL_SCHNAPS_TOWER = 80
    SPECIAL_DUMMFICK = 81

## map drink types with prices to count in points
drinkPriceMapping = {
    "WODKA_PUR": 200,
    "WODKA_ORANGE" : 250,
    "WODKA_BULL": 250,
    "WODKA_UBOOT": 250,

    ####
    "BACARDI_PUR": 250,
    "BACARDI_ORANGE": 250,
    "BACARDI_COLA": 250,

    ####
    "BEER_HALBE": 200,
    "BEER_WEIZEN": 200,
    "BEER_PILS": 200,
    "BEER_STIEFEL": 1200,
    "BEER_MASS": 400,
    "BEER_RADLER": 150,

    ###
    "SHOT_FICKEN": 150,
    "SHOT_BERLINER_LUFT": 150,
    "SHOT_PFEFFI": 150,
    "SHOT_KLOPFER": 150,
    "SHOT_WODKA_BRAUSE": 150,


    ###
    "GIN_TONIC": 250,

    ### Wine
    "WINE_SEKT": 200,
    "WINE_HUGO": 200,
    "WINE_SCHORLE": 200,
    "WINE_FLASCHE": 900,

    ## Captain
    "CAPTAIN_COLA": 250,

    # Non-Alcoholic
    "NOALC_WATER": 150,
    "NOALC_COLA": 150,
    "NOALC_FANTA": 150,
    "NOALC_BULL": 150,
    "NOALC_TONIC": 150,

    #Special
    "SPECIAL_SCHNAPS_TOWER": 2800,
    "SPECIAL_DUMMFICK": 250,
}


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
    "numTeams":         3,          #number of playing teams, currently only 4 players are supported due to GUI limitations
    "teamColors": ['#fc2803', '#03fc77', '#035efc'], #bar colors for the teams
    "teamNames": ["Team ROT", "Team GRÜN", "Team BLAU"],  #team names used for plots

}