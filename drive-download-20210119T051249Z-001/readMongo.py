import pymongo

client=pymongo.MongoClient('mongodb://127.0.0.1:27017/')
myDb = client['bajaj']


def readNodes():
    myCol = myDb['nodeCollection']

    x = myCol.find_one()
    #print(x)
    for key,value in x.items():
        if key == "_id":
            continue
        print(str(key) + " : " + str(value))

def readConnections():
    myCol = myDb['connectionCollection']

    x = myCol.find()
    for data in x:
        for key,value in data.items():
            if str(key)=="_id":
                continue
            print(str(key)+" : " +str(value))
        print("\n")

def searchConnections():
    component = input("Enter component to search: ")
    myCol = myDb['connectionCollection']

    x = myCol.find({'component':str(component)})
    for data in x:
        for key,value in data.items():
            if str(key)=="_id":
                continue
            print(str(key)+" : " +str(value))
        print("\n")


readNodes()
readConnections()
searchConnections()
