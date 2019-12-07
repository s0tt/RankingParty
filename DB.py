from config import plotterConfig, Drinks
from tinydb import TinyDB
from tinydb import Query
import datetime

class DBHandler:
    def __init__(self, dbgMode = False):
        self.dbPath = plotterConfig["dbPath"]
        self.dbgMode = dbgMode
        self.query = Query()
        ###init shared data for GUI
        self.connect()
        self.db.insert({"teamBoosts": 0})
        self.close()

    def connect(self):
        self.db = TinyDB(self.dbPath)
        
    def close(self):
        self.db.close()

    def write(self, teamID, drinkID, drinkNR=1, appendTimeStamp=True):
        self.connect()
        timestamp = datetime.datetime.now().timestamp()
        for i in range(0,drinkNR):
            if appendTimeStamp:
                self.db.insert({"team": teamID, "type": drinkID, "time": timestamp})
            else:
                self.db.insert({"team": teamID, "type": drinkID})
            if self.dbgMode:
                print("Db Insert | Team:", teamID, " Drink:", drinkID, " at ", timestamp)

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
