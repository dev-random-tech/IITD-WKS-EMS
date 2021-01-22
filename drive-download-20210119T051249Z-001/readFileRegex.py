import re

def readNodes(mystr):
    nodes = list()
    nodesDict = {}
    nodes = re.findall(r"\[(.*?)\]",mystr)
    for node in nodes:
        stuff = node.split()
        nodesDict[stuff[0]] = stuff[1]
        #print(stuff[1] + " is represented as " + stuff[0])
    return nodesDict

def readConnections(mystr, nodesList):
    connections = list()
    connectionsDict = {}
    dictList = list()
    connections = re.findall(r"\((.*?)\)",mystr)
    for connection in connections:
        stuff = connection.split()
        if len(stuff)>2:
            stuff.pop(0)
        for node in nodesList:
            if(stuff[0].split('-')[0]==node):
                #print(node + ":" + stuff[0] + " is connected to " + stuff[1])
                if node not in connectionsDict:
                    connectionsDict[node]={}
                connectionsDict[node][stuff[0]] = stuff[1]
            elif(stuff[1].split('-')[0]==node):
                #print(node + ":" + stuff[0] + " is connected to " + stuff[1])
                if node not in connectionsDict:
                    connectionsDict[node]={}
                connectionsDict[node][stuff[1]] = stuff[0]
    for key,value in connectionsDict.items():
        newDict = {}
        newDict['component'] = key
        newDict['connections'] = value
        dictList.append(newDict)
    return dictList

f = open("Sheet_1_2020-07-14_17-50-05.net",'r')
lines = f.readlines()
mystr = ' '.join([line.strip() for line in lines])
allNodes = readNodes(mystr)
print(allNodes)
allConnections = readConnections(mystr, allNodes.keys())
print(allConnections)
