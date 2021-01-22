from pymongo import MongoClient

client = MongoClient("mongodb+srv://vaibhav:vaibhaviitd@freecluster.cssqy.mongodb.net/testdb?retryWrites=true&w=majority")
myDB = client.get_database("bajaj")


def readNodesAtlas():
    myCol = myDB['nodeCollection']

    x = myCol.find_one()
    #print(x)
    for key,value in x.items():
        if key == "_id":
            continue
        print(str(key) + " : " + str(value))

def readConnectionsAtlas():
    myCol = myDB['connectionCollection']

    x = myCol.find()
    for data in x:
        for key,value in data.items():
            if str(key)=="_id":
                continue
            print(str(key)+" : " +str(value))
        print("\n")

def searchConnectionsAtlas():
    component = input("Enter component to search: ")
    myCol = myDB['connectionCollection']

    x = myCol.find({'component':str(component)})
    for data in x:
        for key,value in data.items():
            if str(key)=="_id":
                continue
            print(str(key)+" : " +str(value))
        print("\n")


#readNodes()
#readConnections()
