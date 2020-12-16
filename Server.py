from opcua import Server
import time
from random import randint
import pandas as pd

def power():
    nodesDict["POWERSTATUS"].set_value(1)
    print("Ewon Connected \n")
    print("Press Place Pallet \n")

def pallet():
    if (nodesDict["POWERSTATUS"].get_value()) == 1:
        nodesDict["ENTRY1"].set_value(1)
        print ('Entry Sensor: Pallet Placed \n')
        print("Press Place Order \n")
    else:
        print('Power Off \n')
        print("Press Connect \n")

def order():
    global scan
    if (nodesDict["POWERSTATUS"].get_value()) == 1:
        if (nodesDict["ENTRY1"].get_value()) == 1:
            nodesDict["ORDERSTATUS"].set_value(1)
            print("Order Received \n")
            scanInventory()
            '''if nodesDict["inventoryScanOne"] == 1:
                scanInventory()
            else:
                nodesDict["inventoryScanOne"].set_value(1)
                scanInventory()'''

        else:
            print('Pallet not placed \n')
            print("Press Place Pallet \n")
    else:
        print('Power Off \n')
        print("Press Connect \n")

def scanInventory():
    print('Scanning Inventory \n')
    time.sleep(3)
    nodesDict["SCANDONE"].set_value(1)
    print('Inventory Scanned \n')
    time.sleep(1)
    print ('Inventory Present \n')
    inventory = 6#randint(1,5)
    nodesDict["INVENTORY1"].set_value(inventory)
    print ('Inventory Count: ', inventory, '\n')
    time.sleep(2)
    afterScan()

def afterScan():

    # Stopper will be in the up position
    nodesDict["STOPPINGCYLINDER1UP"].set_value(1)
    print('Stopper: Up \n')

    # Conveyor gets started
    nodesDict["CONVEYOR1STATUS"].set_value(1)
    nodesDict["ENTRY1"].set_value(0)
    print('Conveyor: Started \n')
    time.sleep(4)
    # Pallet will be moving towards operational sensor

    # In between entry sensor and operational sensor, there is intermediate sensor
    # All these are proximity sensors

    # Intermediate sensor checks pallet is moving or not
    nodesDict["INTDIGITALOUTPUT"].set_value(1)
    print('Pallet crossed Intermediate Sensor successfully \n')
    time.sleep(3)

    nodesDict["OPDIGITALOUTPUT"].set_value(1)
    print('Pallet is at Operational Sensor \n')

    # Once pallet reaches operational sensor, conveyor stops.
    nodesDict["CONVEYOR1STATUS"].set_value(0)
    print ('Conveyor: Stopped \n')
    time.sleep(2)

    # Now pneumatic part comes in – to engage pallet from the bottom,
    # pull the pallet for placing the valve body, stopper prevents pallet from moving,
    # lever pushes the pallet down
    # Profile of the valve body is checked.
    # The four sides of the valve body are scanned to check whether
    # it is matching with the profile of the predefined body or not

    # Bottom cylinder will be clamped
    nodesDict["PALLETCLAMPINGCYLINDER1FORWARD"].set_value(1)
    print('Bottom cylinder: Pallet clamped \n')
    print('Clamping cylinder: Pulled out \n')
    time.sleep(3)

    # RFID tag will be read by RFID tag reader
    nodesDict["RFIDPOSITION"].set_value(1)
    print ('RFID reader reads RFID tag \n')
    time.sleep(3)

    operation()

def operation():
    global exitFlag
    # Once it is read that the body is 5 by 2 or 3 by 2,
    # accordingly gripper will pick the particular valve body from tray and place it in the pallet.
    nodesDict["GRIPPER1OPEN"].set_value(1)
    print('Gripper picks the valve body from tray \n')
    print('Valve body placed in the pallet \n')
    time.sleep(6)

    # Once clamping is done, gripper moves where the visions will be focused towards the valve body.
    # Gripper is adjusted to align the vision sensor to the valve body

    # Motor engages with the pallet
    nodesDict["MOTORCYLINDER1FORWARD"].set_value(1)
    print('Motor engages with the pallet \n')
    print('Lever is pushed down for rotation \n')
    time.sleep(2)
    # Using motor, valve body is rotated by 90 degree
    print('Valve body is rotated by 90 degree \n')
    time.sleep(2)

    #Profile is captured
    print('Face 1 is being scanned \n')
    time.sleep(3)
    nodesDict["FACEONE"].set_value(1)

    print('Face 2 is being scanned \n')
    time.sleep(3)
    nodesDict["FACETWO"].set_value(1)

    print('Face 3 is being scanned \n')
    time.sleep(3)
    nodesDict["FACETHREE"].set_value(1)

    print('Face 4 is being scanned \n')
    time.sleep(3)
    nodesDict["FACEFOUR"].set_value(1)

    k = True
    while k == True:

        nodesDict["NUMACCEPTED"].set_value(1)
        time.sleep(3)

        #Once profile is correct, pallet will be disengaged from the operational sensor area and exit
        if nodesDict["NUMACCEPTED"].get_value() == 1:

            print('Profile Matched \n')
            time.sleep(1)

            print('Product Accepted \n')
            time.sleep(1)

            nodesDict["MOTORCYLINDER1BACK"].set_value(1)
            print('Motor Stopped \n')
            print('Lever is pushed up \n')
            time.sleep(2)

            nodesDict["STOPPINGCYLINDER1DOWN"].set_value(1)
            print('Stopper: Down \n')
            time.sleep(2)

            nodesDict["PALLETCLAMPINGCYLINDER1BACK"].set_value(1)
            print('Bottom Cylinder: Pallet Unclamped \n')
            time.sleep(2)

            nodesDict["CONVEYOR1STATUS"].set_value(1)
            print('Conveyor: Started \n')
            time.sleep(2)

            nodesDict["CONVEYOR1STATUS"].set_value(0)
            print('Conveyor: Stopped \n')
            time.sleep(2)

            nodesDict["EXIT1"].set_value(1)
            print('Pallet is at exit \n')
            print('Exit \n')
            exitFlag =1
            time.sleep(3)

            nodesDict["SCANDONE"].set_value(0)

            nodesDict["RFIDPOSITION"].set_value(0)

            nodesDict["INTDIGITALOUTPUT"].set_value(0)

            nodesDict["OPDIGITALOUTPUT"].set_value(0)

            nodesDict["GRIPPER1OPEN"].set_value(0)
            nodesDict["MOTORCYLINDER1BACK"].set_value(0)


            nodesDict["STOPPINGCYLINDER1DOWN"].set_value(0)

            nodesDict["PALLETCLAMPINGCYLINDER1BACK"].set_value(0)

            nodesDict["MOTORCYLINDER1FORWARD"].set_value(0)

            nodesDict["ORDERSTATUS"].set_value(0)

            nodesDict["FACEONE"].set_value(0)

            nodesDict["FACETWO"].set_value(0)

            nodesDict["FACETHREE"].set_value(0)

            nodesDict["FACEFOUR"].set_value(0)

            nodesDict["NUMACCEPTED"].set_value(0)

            nodesDict["EXIT1"].set_value(0)

            #nodesDict["numRejected"].set_value(0)

            print('Press Place Pallet')

            k = False

        # If profile does not match with the standard one, then clamping cylinder retracts.
        # Gripper takes the valve body from pallet and rejects it and places it in the rejection area.
        else:
            nodesDict["numRejected"].set_value(1)
            time.sleep(2)
            print('Profile Not Matched \n')
            time.sleep(2)
            print('Product Rejected \n')
            time.sleep(2)
            nodesDict["GRIPPER1OPEN"].set_value(0)
            print("Gripper places the valve body on rejection tray \n")
            time.sleep(2)

            nodesDict["MOTORCYLINDER1BACK"].set_value(0)

            nodesDict["FACEONE"].set_value(0)

            nodesDict["FACETWO"].set_value(0)
            nodesDict["FACETHREE"].set_value(0)
            nodesDict["FACEFOUR"].set_value(0)

            nodesDict["NUMACCEPTED"].set_value(0)

            nodesDict["EXIT1"].set_value(0)

            nodesDict["numRejected"].set_value(0)

            print('Next valve body is to be picked up \n')
            time.sleep(2)

            operation()
            k = False

def askpallet():
    k = True
    while k == True:
        p = input("Pallet Placed (yes/no): ")
        if (p.lower()=='yes'):
            k= False
            nodesDict["ENTRY1"].set_value(1)
            print ('Entry Sensor: Pallet Placed \n')
            time.sleep(3)
            l = True
            while l == True:
                o = input("Place order (yes/no): ")
                if o.lower() =='yes':
                    nodesDict["ORDERSTATUS"].set_value(1)

                    print("Order Received \n")
                    #if nodesDict["inventoryScanOne"]:
                    scanInventory()
                    break

                elif o.lower() =='no':
                    nodesDict["ORDERSTATUS"].set_value(0)
                    l = True
                else:
                    print("Only 'yes' or 'no' are allowed as input \n")
                    l= True
        elif p.lower() =='no':
            nodesDict["ENTRY1"].set_value(0)
            k = True
        else:
            print("Only 'yes' or 'no' are allowed as input \n")
            k= True

def light():
    nodesDict["lightCurtain1"].set_value(1)
    print("Light curtain breached")
    time.sleep(120)

if __name__ == '__main__':
    global exitFlag
    exitFlag = 0
    nodesDict = {}
    detailsDict = {}
    dataset=pd.read_csv('funcNodes.csv')
    variableNames=dataset.iloc[:,0].values
    nodeList=dataset.iloc[:,0].values
    rightValue=dataset.iloc[:,1].values
    nodeAddress=dataset.iloc[:,2].values
    detailed_df = pd.read_csv('stateNodes.csv')
    varNames = detailed_df.iloc[:,0].values
    rightVal = detailed_df.iloc[:,1].values
    nodeAddr = detailed_df.iloc[:,2].values

    server = Server()
    url = "opc.tcp://localhost:61033"
    server.set_endpoint(url)

    node = server.get_objects_node()
    i = 0
    for (n,address,value) in zip(variableNames,nodeAddress,rightValue):
        nodesDict[n] = node.add_variable(address, n , int(value))
        nodesDict[n].set_writable()
    for (n,address,value)  in zip(varNames,nodeAddr,rightVal):
        detailsDict[n]=node.add_variable(address,n,int(value))
        detailsDict[n].set_writable()
    
    server.start()
    print("Server started \n")
    q = True
    while q == True:
        time.sleep(3)
        v = input("Ewon (on/off): ")
        if (v.lower()=='on'):
            ewon= True
            nodesDict["POWERSTATUS"].set_value(1)
            print('Ewon Connected: ', ewon , '\n')
            print(nodesDict["POWERSTATUS"].get_value())
            q = False
            time.sleep(3)
            askpallet()
        elif v.lower() =='off':
            ewon= False
            nodesDict["POWERSTATUS"].set_value(0)
            print('Ewon Connected: ', ewon )
            print("\n")
            q = True
        else:
            print("Only 'on' or 'off' are allowed as input \n")
            q= True

    if exitFlag == 1:
        askpallet()

else:
    dataset=pd.read_csv('funcNodes.csv')

    variableNames=dataset.iloc[:,0].values
    rightValue=dataset.iloc[:,1].values
    nodeAddress=dataset.iloc[:,2].values
    nodesDict = {}
    detailed_df = pd.read_csv('stateNodes.csv')
    varNames = detailed_df.iloc[:,0].values
    rightVal = detailed_df.iloc[:,1].values
    nodeAddr = detailed_df.iloc[:,2].values
    detailsDict = {}
    server = Server()
    url = "opc.tcp://localhost:61033"
    server.set_endpoint(url)

    node = server.get_objects_node()

    for (n,address,value) in zip(variableNames,nodeAddress,rightValue):
        nodesDict[n] = node.add_variable(address, n , int(value))
        #nodesDict[n].set_writable()

    server.start()
    print("Server started \n")
