import os 
import sys
import matplotlib.pyplot as plt
import numpy as np 
from statistics import mean, stdev

uniMessageCount = {}
biMessageCount = {}



for i in range(4,50,4): 
    uniMessageCount[i] = []
    biMessageCount[i] = [] 
    for j in range(0,10):
        getRingScript = "python3 RandomRings.py --size " + str(i)
        os.system(getRingScript)

        ## Run with unidirectional algorithm and get results 
        uniSimScript = "mpiexec -n " +str(i+1) + " python unidirectionalLE.py --test ../tests/randomRing.txt"
        os.system(uniSimScript) 


        with open("../tests/messageSizeResults.txt") as f:
            lines = f.readlines()
            line = lines[0].split(" ")
            messageCount = line[len(line)-1]
            f.close() 
        uniMessageCount[i].append(int(messageCount))

        ## Run with bidirectional and get results 
        biSimScript = "mpiexec -n " +str(i+1) + " python bidirectionalLE.py --test ../tests/randomRing.txt"
        # os.system(biSimScript) 


        # with open("../tests/messageSizeResults.txt") as f:
        #     lines = f.readlines()
        #     line = lines[0].split(" ")
        #     messageCount = line[len(line)-1]
        #     f.close() 
        # uniMessageCount[i].append(int(messageCount))

xvals = [] 

uniAverage = []
uniStd = [] 

biAverage = [] 
biStd = [] 

for key in uniMessageCount: 
    xvals.append(key)

    uniAverage.append(mean(uniMessageCount[key]))
    uniStd.append(stdev(uniMessageCount[key]))


xvals = np.array(xvals)

uniAverage = np.array(uniAverage)
uniStd = np.array(uniStd)

plt.errorbar(xvals,uniAverage,uniStd,linestyle='None', marker='^')

print(uniMessageCount)
plt.savefig("results")
