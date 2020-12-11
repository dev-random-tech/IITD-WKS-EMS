from opcua import Server
import time
from random import randint
import pandas as pd

def power():
    nodesDict["powerStatus"].set_value(1)
    print("Ewon Connected \n")
    print("Press Place Pallet \n")

def pallet():
    if (nodesDict["powerStatus"].get_value()) == 1:
        nodesDict["entry1"].set_value(1)
        print ('Entry Sensor: Pallet Placed \n')
        print("Press Place Order \n")
    else:
        print('Power Off \n')
        print("Press Connect \n")

def order():
    global scan
    if (nodesDict["powerStatus"].get_value()) == 1:
        if (nodesDict["entry1"].get_value()) == 1:
            nodesDict["orderStatus"].set_value(1)
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
    nodesDict["scanDone"].set_value(1)
    print('Inventory Scanned \n')
    time.sleep(1)
    print ('Inventory Present \n')
    inventory = 6#randint(1,5)
    nodesDict["inventory1"].set_value(inventory)
    print ('Inventory Count: ', inventory, '\n')
    time.sleep(2)
    afterScan()

def afterScan():

    # Stopper will be in the up position
    nodesDict["stoppingCylinder1up"].set_value(1)
    print('Stopper: Up \n')

    # Conveyor gets started
    nodesDict["conveyor1Status"].set_value(1)
    nodesDict["entry1"].set_value(0)
    print('Conveyor: Started \n')
    time.sleep(4)
    # Pallet will be moving towards operational sensor

    # In between entry sensor and operational sensor, there is intermediate sensor
    # All these are proximity sensors

    # Intermediate sensor checks pallet is moving or not
    nodesDict["intDigitalOutput"].set_value(1)
    print('Pallet crossed Intermediate Sensor successfully \n')
    time.sleep(3)

    nodesDict["opDigitalOutput"].set_value(1)
    print('Pallet is at Operational Sensor \n')

    # Once pallet reaches operational sensor, conveyor stops.
    nodesDict["conveyor1Status"].set_value(0)
    print ('Conveyor: Stopped \n')
    time.sleep(2)

    # Now pneumatic part comes in – to engage pallet from the bottom,
    # pull the pallet for placing the valve body, stopper prevents pallet from moving,
    # lever pushes the pallet down
    # Profile of the valve body is checked.
    # The four sides of the valve body are scanned to check whether
    # it is matching with the profile of the predefined body or not

    # Bottom cylinder will be clamped
    nodesDict["palletClampingCylinder1Forward"].set_value(1)
    print('Bottom cylinder: Pallet clamped \n')
    print('Clamping cylinder: Pulled out \n')
    time.sleep(3)

    # RFID tag will be read by RFID tag reader
    nodesDict["rFIDPosition"].set_value(1)
    print ('RFID reader reads RFID tag \n')
    time.sleep(3)

    operation()

def operation():
    global exitFlag
    # Once it is read that the body is 5 by 2 or 3 by 2,
    # accordingly gripper will pick the particular valve body from tray and place it in the pallet.
    nodesDict["gripper1Open"].set_value(1)
    print('Gripper picks the valve body from tray \n')
    print('Valve body placed in the pallet \n')
    time.sleep(6)

    # Once clamping is done, gripper moves where the visions will be focused towards the valve body.
    # Gripper is adjusted to align the vision sensor to the valve body

    # Motor engages with the pallet
    nodesDict["motorCylinder1Forward"].set_value(1)
    print('Motor engages with the pallet \n')
    print('Lever is pushed down for rotation \n')
    time.sleep(2)
    # Using motor, valve body is rotated by 90 degree
    print('Valve body is rotated by 90 degree \n')
    time.sleep(2)

    #Profile is captured
    print('Face 1 is being scanned \n')
    time.sleep(3)
    nodesDict["faceOne"].set_value(1)

    print('Face 2 is being scanned \n')
    time.sleep(3)
    nodesDict["faceTwo"].set_value(1)

    print('Face 3 is being scanned \n')
    time.sleep(3)
    nodesDict["faceThree"].set_value(1)

    print('Face 4 is being scanned \n')
    time.sleep(3)
    nodesDict["faceFour"].set_value(1)

    k = True
    while k == True:

        nodesDict["numAccepted"].set_value(1)
        time.sleep(3)

        #Once profile is correct, pallet will be disengaged from the operational sensor area and exit
        if nodesDict["numAccepted"].get_value() == 1:

            print('Profile Matched \n')
            time.sleep(1)

            print('Product Accepted \n')
            time.sleep(1)

            nodesDict["motorCylinder1Back"].set_value(1)
            print('Motor Stopped \n')
            print('Lever is pushed up \n')
            time.sleep(2)

            nodesDict["stoppingCylinder1down"].set_value(1)
            print('Stopper: Down \n')
            time.sleep(2)

            nodesDict["palletClampingCylinder1Back"].set_value(1)
            print('Bottom Cylinder: Pallet Unclamped \n')
            time.sleep(2)

            nodesDict["conveyor1Status"].set_value(1)
            print('Conveyor: Started \n')
            time.sleep(2)

            nodesDict["conveyor1Status"].set_value(0)
            print('Conveyor: Stopped \n')
            time.sleep(2)

            nodesDict["exit1"].set_value(1)
            print('Pallet is at exit \n')
            print('Exit \n')
            exitFlag =1
            time.sleep(3)

            nodesDict["scanDone"].set_value(0)

            nodesDict["rFIDPosition"].set_value(0)

            nodesDict["intDigitalOutput"].set_value(0)

            nodesDict["opDigitalOutput"].set_value(0)

            nodesDict["gripper1Open"].set_value(0)
            nodesDict["motorCylinder1Back"].set_value(0)


            nodesDict["stoppingCylinder1down"].set_value(0)

            nodesDict["palletClampingCylinder1Back"].set_value(0)

            nodesDict["motorCylinder1Forward"].set_value(0)

            nodesDict["orderStatus"].set_value(0)

            nodesDict["faceOne"].set_value(0)

            nodesDict["faceTwo"].set_value(0)

            nodesDict["faceThree"].set_value(0)

            nodesDict["faceFour"].set_value(0)

            nodesDict["numAccepted"].set_value(0)

            nodesDict["exit1"].set_value(0)

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
            nodesDict["gripper1Open"].set_value(0)
            print("Gripper places the valve body on rejection tray \n")
            time.sleep(2)

            nodesDict["motorCylinder1Back"].set_value(0)

            nodesDict["faceOne"].set_value(0)

            nodesDict["faceTwo"].set_value(0)
            nodesDict["faceThree"].set_value(0)
            nodesDict["faceFour"].set_value(0)

            nodesDict["numAccepted"].set_value(0)

            nodesDict["exit1"].set_value(0)

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
            nodesDict["entry1"].set_value(1)
            print ('Entry Sensor: Pallet Placed \n')
            time.sleep(3)
            l = True
            while l == True:
                o = input("Place order (yes/no): ")
                if o.lower() =='yes':
                    nodesDict["orderStatus"].set_value(1)

                    print("Order Received \n")
                    #if nodesDict["inventoryScanOne"]:
                    scanInventory()
                    break

                elif o.lower() =='no':
                    nodesDict["orderStatus"].set_value(0)
                    l = True
                else:
                    print("Only 'yes' or 'no' are allowed as input \n")
                    l= True
        elif p.lower() =='no':
            nodesDict["entry1"].set_value(0)
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

    dataset=pd.read_csv('NodesCopy.csv')
    variableNames=dataset.iloc[:,0].values
    nodeList=dataset.iloc[:,0].values
    rightValue=dataset.iloc[:,1].values
    nodeAddress=dataset.iloc[:,2].values

    server = Server()
    url = "opc.tcp://localhost:61032"
    server.set_endpoint(url)

    node = server.get_objects_node()
    i = 0
    for (n,address,value) in zip(variableNames,nodeAddress,rightValue):
        nodesDict[n] = node.add_variable(address, n , int(value))
        nodesDict[n].set_writable()
        if i >=23:
            nodesDict[n].set_value(0)
        i = i+1
    
    server.start()
    print("Server started \n")
    q = True
    while q == True:
        time.sleep(3)
        v = input("Ewon (on/off): ")
        if (v.lower()=='on'):
            ewon= True
            nodesDict["powerStatus"].set_value(1)
            print('Ewon Connected: ', ewon , '\n')
            print(nodesDict["powerStatus"].get_value())
            q = False
            time.sleep(3)
            askpallet()
        elif v.lower() =='off':
            ewon= False
            nodesDict["powerStatus"].set_value(0)
            print('Ewon Connected: ', ewon )
            print("\n")
            q = True
        else:
            print("Only 'on' or 'off' are allowed as input \n")
            q= True

    if exitFlag == 1:
        askpallet()

else:
    dataset=pd.read_csv('Nodes.csv')

    variableNames=dataset.iloc[:,0].values
    rightValue=dataset.iloc[:,1].values
    nodeAddress=dataset.iloc[:,2].values
    nodesDict = {}

    server = Server()
    url = "opc.tcp://localhost:61033"
    server.set_endpoint(url)

    node = server.get_objects_node()

    for (n,address,value) in zip(variableNames,nodeAddress,rightValue):
        nodesDict[n] = node.add_variable(address, n , int(value))
        #nodesDict[n].set_writable()

    server.start()
    print("Server started \n")
