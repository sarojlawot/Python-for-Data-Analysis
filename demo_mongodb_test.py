import pymongo

myclient =pymongo.MongoClient("mongodb://localhost:27017/")
#mydb = myclient["mydatabase"]

# database created!
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("the database exists")