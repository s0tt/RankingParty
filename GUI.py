from PyQt5 import QtGui, QtWidgets
import sys
import RankingPartyGUI
from config import Drinks, teamConfig
from DB import DBHandler, Query
from time import time
import math

class RankingPartyApp(QtWidgets.QMainWindow, RankingPartyGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RankingPartyApp, self).__init__(parent)
        self.setupUi(self)

        #setup class
        self.DBHandler = DBHandler(dbgMode=True)
        self.teamSelector = -1
        self.specialIsActive = False

        #setup lists
        self.listListWidgets = [self.wodkaList, self.bacardiList, self.beerList, self.ginList, 
                                self.shotList, self.wineList, self.noalcList, self.specialList, 
                                self.captainList]
        self.DrinksDict = dict((item.name, item.value) for item in Drinks)

        #connect button fcns
        self.pb_Blue.clicked.connect(lambda: self.handleTeamSel(self.pb_Blue))
        self.pb_Green.clicked.connect(lambda: self.handleTeamSel(self.pb_Green))
        self.pb_Red.clicked.connect(lambda: self.handleTeamSel(self.pb_Red))
        self.pb_remove.clicked.connect(lambda: self.removeLogs())
        self.pb_controlMult.clicked.connect(lambda: self.handleMultiplier())

        ### TODO: add dynamic team selection based on team cnt
        #self.pb_Yellow.clicked.connect(lambda: self.handleTeamSel(self.pb_Yellow))

        self.pbClearAmnt.clicked.connect(lambda: self.amntBox.setValue(1))

        #connect list views
        #for listWidget in self.listListWidgets:
        #    listWidget.clicked.connect(lambda: self.handleDrinkSel(listWidget))
        self.wodkaList.clicked.connect(lambda: self.handleDrinkSel(self.wodkaList))
        self.bacardiList.clicked.connect(lambda: self.handleDrinkSel(self.bacardiList))
        self.beerList.clicked.connect(lambda: self.handleDrinkSel(self.beerList))
        self.ginList.clicked.connect(lambda: self.handleDrinkSel(self.ginList))
        self.shotList.clicked.connect(lambda: self.handleDrinkSel(self.shotList))
        self.wineList.clicked.connect(lambda: self.handleDrinkSel(self.wineList))
        self.noalcList.clicked.connect(lambda: self.handleDrinkSel(self.noalcList))
        self.specialList.clicked.connect(lambda: self.handleDrinkSel(self.specialList))
        self.captainList.clicked.connect(lambda: self.handleDrinkSel(self.captainList))


    def handleTeamSel(self, buttonPressed):
        checkedVal = True
        if buttonPressed == self.pb_Blue:
            self.pb_Green.setChecked(checkedVal)
            self.pb_Red.setChecked(checkedVal)
            #self.pb_Yellow.setChecked(checkedVal)
            self.pb_Blue.setChecked(not checkedVal)
            self.teamSelector = 2
        if buttonPressed == self.pb_Green:
            self.pb_Blue.setChecked(checkedVal)
            self.pb_Red.setChecked(checkedVal)
            #self.pb_Yellow.setChecked(checkedVal)
            self.pb_Green.setChecked(not checkedVal)
            self.teamSelector = 1
        if buttonPressed == self.pb_Red:
            self.pb_Green.setChecked(checkedVal)
            self.pb_Blue.setChecked(checkedVal)
            #self.pb_Yellow.setChecked(checkedVal)
            self.pb_Red.setChecked(not checkedVal)
            self.teamSelector = 0
#        if buttonPressed == self.pb_Yellow:
#            self.pb_Green.setChecked(checkedVal)
#            self.pb_Blue.setChecked(checkedVal)
#            self.pb_Red.setChecked(checkedVal)
#            self.pb_Yellow.setChecked(not checkedVal)
#            self.teamSelector = 3
#        print("Selected Team: ", self.teamSelector)

    def handleDrinkSel(self, listWidgetClicked):

        #print(listWidgetClicked.objectName(), " clicked")

        #### manage GUi displaying
        for listWidget in self.listListWidgets:
            if listWidget != listWidgetClicked:
                #print(listWidget.objectName(), " cleared")
                listWidget.clearSelection()
                #listWidget.clearFocus()
        
        #### check for team selection
        if self.teamSelector < 0:
            print("Please select a team first!")
            return

        #### manage selected drink
        widgetName = str(listWidgetClicked.objectName()).replace('List','')
        itemName = str(listWidgetClicked.currentItem().text())
        ##replace spaces with underscores
        itemName = itemName.replace(' ', '_')
        drinkStr = widgetName.upper() + "_" + itemName.upper()
        
        self.drinkID = self.DrinksDict[drinkStr]
        #print(drinkStr, " ", drinkID)

        self.pushDB()

    def removeLogs(self):
        #function to remove selected logs from db& view
        for selectedItem in self.logList.selectedItems():
            idx = selectedItem.text().split("=")[1]
            self.DBHandler.removeByIdx(idx)
            #self.logList.takeItem(selectedItem.row())

    def pushDB(self):
        #### push to database
        drinkAmount = self.amntBox.value()
        idx = self.DBHandler.write(self.teamSelector, self.drinkID, drinkNR=drinkAmount)

        ### display pushed data in log box
        teamNames = teamConfig["teamNames"]
        printStr = str(teamNames[self.teamSelector].replace("\n"," "))+" | Pkt: "+str(self.drinkID)+" | IDX=" + str(idx)
        self.logList.addItem(printStr)
        if self.logList.count() > 10:
            self.logList.takeItem(10)

    def handleMultiplier(self):
        if self.specialIsActive:
            ### special active
            self.DBHandler.updateById( {
                        'isActive': 0,
                        'boost_red': 1.0, 
                        'boost_green': 1.0,
                        'boost_blue': 1.0
                        }, [1])
            self.pb_controlMult.setText("Activate")
            self.specialIsActive = False

        else:
            ### special not yet active
            self.pb_controlMult.setChecked
            multiplierVal = self.sb_multiplier.value()
            multiplierList = [0, 0, 0]
            for idx, cbItem in enumerate([self.cb_red, self.cb_green, self.cb_blue]):
                if cbItem.isChecked() is True:
                    multiplierList[idx] = multiplierVal

            
            self.DBHandler.updateById( {
                                    'isActive': 1,
                                    'boost_red':multiplierList[0], 
                                    'boost_green':multiplierList[1],
                                    'boost_blue': multiplierList[2]
                                    }, [1])
            self.pb_controlMult.setText("Deactivate")                        
            self.specialIsActive = True
                
                
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = RankingPartyApp()
    form.show()
    app.exec_()

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function