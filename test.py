from opcua import Client


url = "opc.tcp://localhost:61031"
client = Client(url)

client.connect()
print("Client Connected \n")

nodeDict = {}
nodeDict["power"] = client.get_node("ns=3;s=[PLC]power_on")
#node = client.get_node("ns=3;s=[PLC]power_on")

while True:
	print(nodeDict["power"].get_value())
	print(nodeDict["power"])
