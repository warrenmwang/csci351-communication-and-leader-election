import argparse
import random


parser = argparse.ArgumentParser() 
parser.add_argument("--size",help = "Number of processes in ring graph")
args = parser.parse_args() 
size = int(args.size)

processes = []
orderedProcesses = [] 
neighbors = []

for i in range(0,size):
    processes.append(i)
    neighbors.append([])



firstNode = random.choice(processes)
curNode = firstNode 
processes.remove(curNode)

orderedProcesses.append(firstNode)
while (len(processes) > 0): 
    firstNeighbor = random.choice(processes)
    processes.remove(firstNeighbor)
    neighbors[curNode].append(firstNeighbor)
    orderedProcesses.append(firstNeighbor)
    curNode = firstNeighbor

neighbors[curNode].append(firstNode)

for i in range(len(orderedProcesses)-1,0,-1): 
    curNode = orderedProcesses[i] 

    neighbors[curNode].append(orderedProcesses[i-1])

firstNode = orderedProcesses[0]
neighbors[firstNode].append(len(orderedProcesses)-1)

print(neighbors)


textString = ""
for i in range(len(neighbors)):
    textString += str(i)+": " + str(neighbors[i][0]) + ", " + str(neighbors[i][1]) + "\n" 

f = open("../tests/randomRing.txt","w")
f.write(textString)
f.close()





