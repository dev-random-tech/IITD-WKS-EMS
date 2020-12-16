from opcua import Client
import time
from datetime import datetime
import csv
import pandas as pd
import numpy as np
from numpy import nan
import datetime as now
from numpy import isnan
from pandas import read_csv
from pandas import to_numeric
from threading import Thread, Event
from operator import and_
from operator import not_
import re

def all_check(tag_list):
    return sum(tag_list)

def mul(a,b):  # Returns 1 if both values are same
    if a == b:
        return 1
    else:
        return 0

def reasons(nameTags):
    regex_queries = []
    for i in nameTags:
        string = "^"+i+"_*"
        regex_queries.append(string)
    for j in range(len(nameTags)):
        for k in detailsDict.keys():
            if re.search(regex_queries[j],k):
#                print(detailsDict[k].get_value())
#                print(rightValDict[k])
                if rightValDict[k] != detailsDict[k].get_value():
                    print("Reason for Error:",k)


def faults(tags, event_num):
    op = list(map(mul, tags, list(correct_tags[event_num, :])))
    if all_check(op) != len(tags):
        faults = list(map(bool, op))
        faults = list(map(not_, faults))
        print('Faults at:', tag_names[faults])
        reasons(tag_names[faults])

def updateValues():
    global updateFlag
    global data_array
    global time_array
    updateFlag = False
    eventCounter = 0
    while True:
        if updateFlag:
            updateFlag = False
            if ewon is True:
                tagList = []
                detailedList = []
                for key in nodesDict:
                    tagList.append(nodesDict[key].get_value())

                print('EventNum: ', eventCounter)
                #time_array.append(datetime.now())
                faults(tagList, eventCounter)
                # print(tagList)
                #if eventCounter == 0:
                    #tag_list = np.array(tagList)
                    #data_array = np.append(data_array, tagList, axis=0)
                #else:
                    #data_array = np.vstack((data_array, tagList))

                eventCounter = eventCounter+1


def datafile():
    global variableNames
    global data_array
    global time_array
    df_db = pd.DataFrame(data=data_array, columns=variableNames)
    df_db['TIMESTAMPS'] = time_array
    filename = 'correct_tags.csv'
    df_db.to_csv(filename, index=False)

# Subscription of events


class SubHandler(object):
    def datachange_notification(self, node, val, data):
        global flag
        global ewon
        global updateFlag
        updateFlag = True

        if node == nodesDict["POWERSTATUS"]:
            if val == 1:
                ewon = True
                print('Ewon Connected \n')
                print('Waiting for the status of pallet \n')
                print('Press Place Pallet \n')
            else:
                print('Power off')
        elif node == nodesDict["ORDERSTATUS"]:
            if val == 1:
                print('Order Status: Order Received \n')

        elif node == nodesDict["SCANDONE"]:
            if val == 1:
                print('Inventory Scan Done \n')

        elif node == nodesDict["INVENTORY1"]:
            if ewon == True:
                print('Inventory Present \n')
                print('Inventory Count: ', val, '\n')

        elif node == nodesDict["STOPPINGCYLINDER1UP"]:
            if val == 1:
                print('Stopper: Up \n')

        elif node == nodesDict["STOPPINGCYLINDER1DOWN"]:
            if val == 1 and ewon == True:
                print('Stopper: Down \n')

        elif node == nodesDict["CONVEYOR1STATUS"]:
            if val == 1:
                print('Conveyor: Started \n')
            elif val == 0 and ewon == True:
                print('Conveyor: Stopped \n')

        elif node == nodesDict["INTDIGITALOUTPUT"]:
            if val == 1:
                print('Pallet crossed Intermediate Sensor successfully \n')

        elif node == nodesDict["OPDIGITALOUTPUT"]:
            if val == 1:
                print('Pallet is at Operational Sensor \n')

        elif node == nodesDict["PALLETCLAMPINGCYLINDER1FORWARD"]:
            if val == 1:
                print('Bottom cylinder: Pallet Clamped \n')
                print('Clamping cylinder: Pulled out \n')

        elif node == nodesDict["PALLETCLAMPINGCYLINDER1BACK"]:
            if val == 1 and ewon == True:
                print('Bottom cylinder: Pallet Unclamped \n')

        elif node == nodesDict["RFIDPOSITION"]:
            if val == 1:
                print('RFID reader reads RFID tag \n')

        elif node == nodesDict["GRIPPER1OPEN"]:
            if val == 1:
                print('Gripper picks the valve body from tray \n')
                print('Valve body placed in the pallet \n')

        elif node == nodesDict["MOTORCYLINDER1FORWARD"]:
            if val == 1:
                print('Motor engages with the pallet \n')
                print('Lever is pushed down for rotation \n')
                print('Valve body is rotated by 90 degree \n')

        elif node == nodesDict["MOTORCYLINDER1BACK"]:
            if val == 1 and ewon == True:
                print('Motor Stopped \n')
                print('Lever is pushed up \n')

        elif node == nodesDict["FACEONE"]:
            if val == 1:
                print('Face 1 scanned \n')

        elif node == nodesDict["FACETWO"]:
            if val == 1:
                print('Face 2 scanned \n')

        elif node == nodesDict["FACETHREE"]:
            if val == 1:
                print('Face 3 scanned \n')

        elif node == nodesDict["FACEFOUR"]:
            if val == 1:
                print('Face 4 scanned \n')

        elif node == nodesDict["NUMACCEPTED"]:
            if val == 1:
                print('Profile Matched \n')

        elif node == nodesDict["ENTRY1"]:
            if val == 1 and ewon == True:
                print('Entry Sensor: Pallet Placed \n')
                print('Waiting for the order \n')
                print('Press Place Order \n')

        elif node == nodesDict["EXIT1"]:
            if val == 1:
                print('Pallet is at exit \n')
                print('Exit \n')
                # datafile()
                flag = False

        '''elif node == nodesDict["numRejected"]:
            if val == 1:
                print('Profile Not Matched \n')
                print('Profile Rejected \n')'''


def main():
    try:
        #powerUrl = "opc.tcp://10.226.52.200:4840"
        #clientEwon = Client(powerUrl)
        #powerEwon = clientEwon.get_node("ns=4;s=power")

        # machine1 url uncomment it
        #url = "opc.tcp://10.226.52.227:4994"
        url = "opc.tcp://localhost:61033"
        client = Client(url)
        for (n, address, value) in zip(variableNames, nodeAddress, rightValue):
            nodesDict[n] = client.get_node(address)

        for (n, address, value) in zip(varNames, nodeAddr, rightVal):
            detailsDict[n] = client.get_node(address)
            rightValDict[n] = value
        print(rightValDict)
        # uncomment  when running on actual macine # for ewon
        #nodesDict["POWERSTATUS"] = clientEwon.get_node("ns=4;s=power")
        client.connect()
        print("Client Connected \n")
        print('Press Connect \n')

        sub = client.create_subscription(100, SubHandler())
        #h = sub.subscribe_events()
        for item in nodesDict:
            if item == 'smps1':
                break
            handle = sub.subscribe_data_change(nodesDict[item])

    except ConnectionResetError:
        print("ConnectionResetError")
    except ConnectionRefusedError:
        print("ConnectionRefusedError: Server not started")
    except ConnectionError:
        print('ConnectionError')
    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        print(message)
    # finally:
        # print("")
        # sub.unsubscribe(handle)
        # client.disconnect


if __name__ == '__main__':

    flag = True
    ewon = False
    nodeList = []
    valuesList = []
    timeList = []
    nodesDict = {}
    detailsDict = {}
    rightValDict = {}
    data_array = np.array([])
    time_array = []

    try:
        dataset = pd.read_csv('funcNodes.csv')
        variableNames = dataset.iloc[:, 0].values
        rightValue = dataset.iloc[:, 1].values
        nodeAddress = dataset.iloc[:, 2].values
        detailed_df = pd.read_csv('stateNodes.csv')
        varNames = detailed_df.iloc[:, 0].values
        rightVal = detailed_df.iloc[:, 1].values
        nodeAddr = detailed_df.iloc[:, 2].values
        ct_df = pd.read_csv('correct_tags.csv')
        correct_tags = ct_df.loc[:, "POWERSTATUS":"EXIT1"].values
        #print(correct_tags)
        temp = np.asarray(ct_df.columns)
        #print(temp)
        tag_names = np.delete(temp, -1)
        #print(tag_names)
        stateTags_df = pd.read_csv('stateNodes.csv')
        varNames = stateTags_df.iloc[:, 0].values
        varNames = np.asarray(varNames)
        rightVals = list(stateTags_df.iloc[:, 1].values)

    except FileNotFoundError:
        print("File not found")

    except PermissionError:
        print("You don't have the permission to read the file")

    except:
        print("Unexpected error while reading the file")

    thread2 = Thread(target=main)
    thread2.start()

    thread1 = Thread(target=updateValues)
    thread1.start()

    thread2.join()
    thread1.join()
