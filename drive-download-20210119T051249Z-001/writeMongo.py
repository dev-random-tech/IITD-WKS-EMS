import pymongo

def writeData(allNodes,allConnections):
    client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
    myDb = client['bajaj']

    nodeCollection=myDb.nodeCollection
    nodeCollection.insert_one(allNodes)
    
    connectionCollection=myDb.connectionCollection
    connectionCollection.insert_many(allConnections)