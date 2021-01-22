import re

nodes = list()
connections = list()

f = open("Sheet_1_2020-07-14_17-50-05.net",'r')
lines = f.readlines()
mystr=""

for line in lines:
    ##print(line.strip())
    if line.strip() == ']':
        mystr+=line.strip()
        nodes.append(mystr)
        mystr=""
    elif line.strip()==')':
        mystr+=line.strip()
        connections.append(mystr)
        mystr=""
    else:
        mystr+=line.strip()+" "


##node = re.findall('^\[(.*?)\]',mystr)
##print(node)

print("\nNodes:")
print("********************************************\n")
for node in nodes:
    #print(node)
    stuff = node[2:-5].split()
    print(stuff)
    #print(stuff[1] + " is represented as " + stuff[0])

print("\n\nConnections:")
print("********************************************\n")
for connection in connections:
    #print(connection)
    stuff = connection[2:-1].strip().split()
    if len(stuff)>2:
        print(stuff[1] + " is connected to " + stuff[2])
    else:
        print(stuff[0] + " is connected to " + stuff[1])
