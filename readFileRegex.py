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

def searchConnections(searchItem,searchType,connections):
#   For checking IOL connections
    searchQuery = searchItem+"-"+searchType+"*"
    for j in connections[searchItem].keys():
        if re.search(searchQuery,j):
            print(j,"->",connections[searchItem][j])

#f = open("sensor use case.net",'r')
#lines = f.readlines()
#mystr = ' '.join([line.strip() for line in lines])
#allNodes = readNodes(mystr)
#inv_Nodes = {a:b for b,a in allNodes.items()}
#allConnections = readConnections(mystr, allNodes.keys())
#newConnections = {}
#for y in allConnections:
#    newConnections[y['component']] = y['connections']

'''
{'IOL': 'IO_Link', '24V_COM_TERMINAL': 'Terminal', '24V_TERMINAL': 'Terminal', 'OPERATIONAL_SENSOR': 'Proximity', 'GND': 'Ground'}
[{'component': 'IOL', 'connections': {'IOL-power_COM_2': '24V_COM_TERMINAL-1', 'IOL-power_24V_1': '24V_TERMINAL-1', 'IOL-Port2_24V': 'OPERATIONAL_SENSOR-24Vsupply', 'IOL-Port2_24VCOM': 'OPERATIONAL_SENSOR-24VCOMsupply', 'IOL-Port2_Output': 'OPERATIONAL_SENSOR-Outputsupply', 'IOL-power_COM_3': '24V_COM_TERMINAL-3', 'IOL-power_24V_4': '24V_TERMINAL-3', 'IOL-FN_GND_5': 'GND-1'}}, {'component': '24V_COM_TERMINAL', 'connections': {'24V_COM_TERMINAL-1': 'IOL-power_COM_2', '24V_COM_TERMINAL-3': 'IOL-power_COM_3', '24V_COM_TERMINAL-2': '0V'}}, {'component': '24V_TERMINAL', 'connections': {'24V_TERMINAL-1': 'IOL-power_24V_1', '24V_TERMINAL-3': 'IOL-power_24V_4', '24V_TERMINAL-2': '+24V'}}, {'component': 'OPERATIONAL_SENSOR', 'connections': {'OPERATIONAL_SENSOR-24Vsupply': 'IOL-Port2_24V', 'OPERATIONAL_SENSOR-24VCOMsupply': 'IOL-Port2_24VCOM', 'OPERATIONAL_SENSOR-Outputsupply': 'IOL-Port2_Output'}}, {'component': 'GND', 'connections': {'GND-1': 'IOL-FN_GND_5'}}]
'''
