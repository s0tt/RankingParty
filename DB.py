from config import plotterConfig, Drinks, drinkPriceMapping
from tinydb import TinyDB
from tinydb import Query
import datetime
import math
import uuid

class DBHandler:
    def __init__(self, dbgMode = False):
        self.dbPath = plotterConfig["dbPath"]
        self.dbgMode = dbgMode
        self.query = Query()
        ###init shared data for GUI
        if self.readById(1) is None:
            self.connect()
            self.db.insert({"isActive": 0, "boost_red": 0, "boost_green": 0, "boost_blue": 0})
            self.close()

    def connect(self):
        self.db = TinyDB(self.dbPath)
        
    def close(self):
        self.db.close()

    def write(self, fields):
        self.connect()
        self.db.insert(fields)
        self.db.close()

    def writeDrinks(self, teamID, drinkID, multiplierList, drinkNR=1, appendTimeStamp=True):
        timestamp = datetime.datetime.now().timestamp()
        drinkType = Drinks(drinkID)
        finalDrinkPts = drinkPriceMapping[drinkType.name] * multiplierList[teamID]
        for i in range(0,drinkNR):
            if appendTimeStamp:
                self.write({"team": teamID, "type": drinkID, "pts": finalDrinkPts, "time": timestamp})
            else:
                self.write({"team": teamID, "type": drinkID, "pts": finalDrinkPts})
            if self.dbgMode:
                print("Db Insert | Team:", teamID, " Drink:", drinkType.name, " at ", timestamp)
        self.connect()
        idx = len(self.db.all())
        self.close()
        return idx

    def removeByIdx(self, idx):
        self.connect()
        self.db.remove(doc_ids=[idx])
        self.close()

    def removeByQuery(self, query):
        self.connect()
        self.db.remove(query)
        self.close() 
        

    def read(self, query):
        self.connect()
        response = self.db.search(query)
        self.close()
        return response
    
    def readById(self, id):
        self.connect()
        response = self.db.get(doc_id=id)
        self.close()
        return response

    def readAll(self):
        self.connect()
        response = self.db.all()
        self.close()
        return response

    def updateById(self,fields,ids):
        self.connect()
        response = self.db.update(fields, doc_ids=ids)
        self.close()
        return response
