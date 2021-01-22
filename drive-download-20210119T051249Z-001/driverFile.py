from readFileRegex import *
#from writeMongoAtlas import writeDataAtlas
#from writeMongo import writeData
#from readMongo import *
from readMongoAtlas import *

#f = open("Sheet_1_2020-07-14_17-50-05.net",'r')
#lines = f.readlines()
#mystr = ' '.join([line.strip() for line in lines])

#allNodes = readNodes(mystr)
#allConnections = readConnections(mystr, allNodes.keys())

#will store in local mongoDB
#writeData(allNodes,allConnections)

#will store in mongoDB Atlas
#writeDataAtlas(allNodes,allConnections)

#readNodes()
#print("\n")
#readConnections()
#print("\n")
#searchConnections()

#readNodesAtlas()
#print("\n")
#readConnectionsAtlas()
#print("\n")
searchConnectionsAtlas()
