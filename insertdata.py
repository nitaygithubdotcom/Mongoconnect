import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["customersdb"]
customers = db["customers"]

def insertdatadb(data):
    customers.insert(data)

def updatedata(data):
    db.customers.update(data)

