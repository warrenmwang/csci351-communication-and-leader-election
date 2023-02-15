from mpi4py import MPI
import argparse
import sys
sys.path.insert(1,"..")
from utils import read_graph



parser  = argparse.ArgumentParser() 
parser.add_argument("--test", help="test file (graph in adjacency list form)")
args = parser.parse_args()
testfile = args.test

#Get testfile from args. For the unidirectional algorithm the graph.txt file is in the form of: rank: left, right and this 
#algorithm always sends to the left neighbor. 

comm = MPI.COMM_WORLD 

rank = comm.Get_rank() 

neighbors = read_graph(testfile,rank)
##The left neighbor is always neighbors[0]



terminateNonLeader = False
comm.isend((rank,terminateNonLeader), dest = neighbors[0])
#Initially send a message that is of type tuple where tuple = (rank,terminateNonLeader) and terminateAsNon Leader is bool 
#flagging if the message being sent should have the receiving process terminate 



while True: 
    recvRequest = comm.irecv()
    while True: 
        recvData = recvRequest.test()
        if recvData[0]:
            break 

    ##ID received is index 1 of recvData and index 0 of the tuple
    recvID = recvData[1][0]
    terminateNonLeader = recvData[1][1]
    print(f"process {rank} received id: {recvID}")
    
    if terminateNonLeader: 
        #if terminateNonLeader is true pass message on and terminate 
        print(f"process {rank} terminated NONLEADER")
        comm.isend((rank,True), dest = neighbors[0])
        sys.exit()
    if recvID != rank: 
        #If receiving ID != rank 
        if recvID > rank: 
            #Pass received ID to left process if it is greater than own ID 
            print(f"{rank} Passing {recvID} to {neighbors[0]}")
            comm.isend((recvID,False), dest = neighbors[0])
    elif recvID == rank: 
        #If recvID == rank, this process is leader, send message to left node with terminateAsNonleader = true, and terminate
        leader = True
        print(f"{rank} has terminated as LEADER")
        comm.isend((rank,True), dest = neighbors[0])
        sys.exit() 
    
