from PyQt5 import QtGui, QtWidgets
import sys
import RankingPartyGUI
from config import Drinks
from DB import DBHandler

class RankingPartyApp(QtWidgets.QMainWindow, RankingPartyGUI.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RankingPartyApp, self).__init__(parent)
        self.setupUi(self)

        #setup class
        self.DBHandler = DBHandler(dbgMode=True)
        self.teamSelector = -1

        #setup lists
        self.listListWidgets = [self.wodkaList, self.bacardiList, self.beerList, self.ginList, self.shotList]
        self.DrinksDict = dict((item.name, item.value) for item in Drinks)

        #connect button fcns
        self.pb_Blue.clicked.connect(lambda: self.handleTeamSel(self.pb_Blue))
        self.pb_Green.clicked.connect(lambda: self.handleTeamSel(self.pb_Green))
        self.pb_Red.clicked.connect(lambda: self.handleTeamSel(self.pb_Red))
        self.pb_Yellow.clicked.connect(lambda: self.handleTeamSel(self.pb_Yellow))
        self.pbClearAmnt.clicked.connect(lambda: self.amntBox.setValue(1))

        #connect list views
        #for listWidget in self.listListWidgets:
        #    listWidget.clicked.connect(lambda: self.handleDrinkSel(listWidget))
        self.wodkaList.clicked.connect(lambda: self.handleDrinkSel(self.wodkaList))
        self.bacardiList.clicked.connect(lambda: self.handleDrinkSel(self.bacardiList))
        self.beerList.clicked.connect(lambda: self.handleDrinkSel(self.beerList))
        self.ginList.clicked.connect(lambda: self.handleDrinkSel(self.ginList))
        self.shotList.clicked.connect(lambda: self.handleDrinkSel(self.shotList))


    def handleTeamSel(self, buttonPressed):
        checkedVal = True
        if buttonPressed == self.pb_Blue:
            self.pb_Green.setChecked(checkedVal)
            self.pb_Red.setChecked(checkedVal)
            self.pb_Yellow.setChecked(checkedVal)
            self.pb_Blue.setChecked(not checkedVal)
            self.teamSelector = 0
        if buttonPressed == self.pb_Green:
            self.pb_Blue.setChecked(checkedVal)
            self.pb_Red.setChecked(checkedVal)
            self.pb_Yellow.setChecked(checkedVal)
            self.pb_Green.setChecked(not checkedVal)
            self.teamSelector = 2
        if buttonPressed == self.pb_Red:
            self.pb_Green.setChecked(checkedVal)
            self.pb_Blue.setChecked(checkedVal)
            self.pb_Yellow.setChecked(checkedVal)
            self.pb_Red.setChecked(not checkedVal)
            self.teamSelector = 1
        if buttonPressed == self.pb_Yellow:
            self.pb_Green.setChecked(checkedVal)
            self.pb_Blue.setChecked(checkedVal)
            self.pb_Red.setChecked(checkedVal)
            self.pb_Yellow.setChecked(not checkedVal)
            self.teamSelector = 3
        print("Selected Team: ", self.teamSelector)

    def handleDrinkSel(self, listWidgetClicked):

        print(listWidgetClicked.objectName(), " clicked")

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

    def pushDB(self):
        #### push to database
        self.DBHandler.write(self.teamSelector, self.drinkID, drinkNR=self.amntBox.value())
        
        
def main():
    app = QtWidgets.QApplication(sys.argv)
    form = RankingPartyApp()
    form.show()
    app.exec_()

if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function