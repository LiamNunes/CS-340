import pymongo
from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelterCRUD (object):
    """ CRUD operations for Animal collection in MongoDB """
    
    def __init__(self, usrname, psswrd):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections. 
        self.client = MongoClient()
        self.client = MongoClient('mongodb://%s:%s@localhost:36771/AAC' % (usrname, psswrd))
        self.db = self.client.AAC
        
    #this method implements the C in CRUD
    def create(self, data):
        try:
            self.db.animals.insert_one(data)
            return True
        except:
            return False
        
    #this method implements the R in CRUD
    def read(self, search):
        try:
            result = self.db.animals.find(search, {"_id":False})
            if (result.count() != 0):
                return result
            else:
                return "error- can not find search entry"
        except:
            return "error- can not find search entry"
        
    #this method implements the U in CRUD
    def update(self, search, data):
        if (self.read(search) != "error- can not find search entry"):
            result = self.db.animals.update_many(search, {'$set': data})
            return result
        else:
            return "error- can not delete entry"
        
    #this method implements the D in CRUD
    def delete(self, search):
        if (self.read(search) != "error- can not find search entry"):
            result = self.db.animals.delete_many(search)
            return result
        else:
            return "error- can not delete entry"