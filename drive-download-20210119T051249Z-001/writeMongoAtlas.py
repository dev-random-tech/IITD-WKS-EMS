from pymongo import MongoClient

def writeDataAtlas(allNodes,allConnections):
    client = MongoClient("mongodb+srv://vaibhav:vaibhaviitd@freecluster.cssqy.mongodb.net/testdb?retryWrites=true&w=majority")
    myDB = client.get_database("bajaj")
    nodeCollection = myDB.get_collection("nodeCollection")
    nodeCollection.insert_one(allNodes)
    connectionCollection = myDB.get_collection("connectionCollection")
    connectionCollection.insert_many(allConnections)
