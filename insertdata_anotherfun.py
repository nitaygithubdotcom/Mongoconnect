from insertdata import insertdatadb
from insertdata import updatedata

user = {"Name":'Nitay','address':"kestopur",'age':25}
db.customers.update({"Name":user["Name"]},{$set:{user}})
insertdatadb()


# customers_list = [
#   { "name": "Amy", "address": "Apple st 652","age":23},
#   { "name": "Hannah", "address": "Mountain 21","age":22},
#   { "name": "Amy", "address": "Valley 345","age":24},
#   { "name": "Viola", "address": "Ocean blvd 2","age":25},
#   { "name": "Amy", "address": "Green Grass 1","age":29},
#   { "name": "Amy", "address": "Sky st 331","age":21},
#   { "name": "Viola", "address": "One way 98","age":23},
#   { "name": "Amy", "address": "Yellow Garden 2","age":23},
#   { "name": "Ben", "address": "Park Lane 38","age":30},
#   { "name": "Amy", "address": "Central st 954","age":32},
#   { "name": "Amy", "address": "Main Road 989","age":20},
#   { "name": "Viola", "address": "Sideway 1633","age":28}
# ]
# insertdatadb(customers_list)

# import pymongo
# client = pymongo.MongoClient("mongodb://172.1.2.0:27017/")
# db = client["customersdb"]
# customers = db["customers"]
# for x in customers.find():
#     print(x)