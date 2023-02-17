from mpi4py import MPI
import argparse
import sys
sys.path.insert(1,"..")
from utils import read_graph

parser  = argparse.ArgumentParser()
parser.add_argument("--test", help="test file (graph in adjacency list form)")
args = parser.parse_args()
testfile = args.test

comm = MPI.COMM_WORLD
size = comm.Get_size()-1
rank = comm.Get_rank()

if rank == size:
    countMessagesRecieved = 0
    totalMessages = 0
    while True:
        recvRequest = comm.irecv()
        while True:
            recvData = recvRequest.test()
            if recvData[0]:
                break
        totalMessages += recvData[1]
        countMessagesRecieved += 1
        if countMessagesRecieved == size:
            print(f"Total number of messages is {totalMessages} ")
            sys.exit()

else:
    neighbors = read_graph(testfile,rank)

    rnd = 0
    dist = 1
    probe = True
    reply = False
    alreadyRecievedLeft = False
    alreadyRecievedRight = False
    leader = False
    terminateNonLeader = False
    numMessages = 0


    comm.isend((rank, rnd, dist, probe, reply, terminateNonLeader, 1), dest = neighbors[0])
    comm.isend((rank, rnd, dist, probe, reply, terminateNonLeader, 0), dest = neighbors[1])

    numMessages+=2

    while True:
        recvRequest = comm.irecv()
        while True:
            recvData = recvRequest.test()
            if recvData[0]:
                break

        ##ID received is index 1 of recvData and index 0 of the tuple
        recvID = recvData[1][0]
        rndNum = recvData[1][1]
        distance = recvData[1][2]
        probe = recvData[1][3]
        reply = recvData[1][4]
        terminateNonLeader = recvData[1][5]
        direction = recvData[1][6]

        if direction == 0
            if terminateNonLeader:

                    #if terminateNonLeader is true pass message to both neigbhors and terminate

                    print(f"process {rank} terminated NONLEADER")
                    #comm.isend((rank, rnd, dist, False, False, terminateNonLeader), dest = neighbors[0])
                    comm.isend((rank, rnd, dist, False, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1
                    comm.isend(numMessages, dest = size)
                    sys.exit()

            #upon receiving probe, j, r, d from left/right
            if probe and reply == False:

                #if process recieves its own id, elect itself as leader
                if recvID == rank and leader == False:
                    leader = True
                    print(f"process {rank} has terminated as LEADER")
                    #comm.isend((rank, rnd, dist, False, reply, True, 1), dest = neighbors[0])
                    comm.isend((rank, rnd, dist, False, reply, True, 0), dest = neighbors[1])
                    numMessages+=1
                    comm.isend(numMessages, dest = size)
                    sys.exit()

                if recvID > rank and distance < pow(2, rndNum):
                    #send probe, j, r, d + 1 to right/left (resp.)
                    #comm.isend((recvID, rndNum, distance+1, True, False, terminateNonLeader, 1), dest = neighbors[0])
                    comm.isend((recvID, rndNum, distance+1, True, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                if recvID > rank and distance >= pow(2, rndNum):
                    #send reply, j, r, to left/right (resp.)
                    #comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader), dest = neighbors[0])
                    comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1


            #On receiving reply, j, r from left/right
            if reply:

                if recvID != rank:
                    #send reply,j,r to right/left (resp.)
                    #comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader), dest = neighbors[0])
                    comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                #already received reply, j, r from right/left (resp.)
                elif reply and alreadyRecievedLeft == True:
                    #send probe, i, r + 1 to left and right
                    #comm.isend((rank, rndNum+1, 1, True, False, terminateNonLeader), dest = neighbors[0])
                    comm.isend((rank, rndNum+1, 1, True, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                alreadyRecievedLeft = True

        if direction == 1
            if terminateNonLeader:

                    #if terminateNonLeader is true pass message to both neigbhors and terminate

                    print(f"process {rank} terminated NONLEADER")
                    comm.isend((rank, rnd, dist, False, False, terminateNonLeader, 1), dest = neighbors[0])
                    #comm.isend((rank, rnd, dist, False, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1
                    comm.isend(numMessages, dest = size)
                    sys.exit()

            #upon receiving probe, j, r, d from left/right
            if probe and reply == False:

                #if process recieves its own id, elect itself as leader
                if recvID == rank and leader == False:
                    leader = True
                    print(f"process {rank} has terminated as LEADER")
                    comm.isend((rank, rnd, dist, False, reply, True, 1), dest = neighbors[0])
                    #comm.isend((rank, rnd, dist, False, reply, True, 0), dest = neighbors[1])
                    numMessages+=1
                    comm.isend(numMessages, dest = size)
                    sys.exit()

                if recvID > rank and distance < pow(2, rndNum):
                    #send probe, j, r, d + 1 to right/left (resp.)
                    comm.isend((recvID, rndNum, distance+1, True, False, terminateNonLeader, 1), dest = neighbors[0])
                    #comm.isend((recvID, rndNum, distance+1, True, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                if recvID > rank and distance >= pow(2, rndNum):
                    #send reply, j, r, to left/right (resp.)
                    comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 1), dest = neighbors[0])
                    #comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1


            #On receiving reply, j, r from left/right
            if reply:

                if recvID != rank:
                    #send reply,j,r to right/left (resp.)
                    comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 1), dest = neighbors[0])
                    #comm.isend((recvID, rndNum, distance, False, True, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                #already received reply, j, r from right/left (resp.)
                elif reply and alreadyRecievedRight == True:
                    #send probe, i, r + 1 to left and right
                    comm.isend((rank, rndNum+1, 1, True, False, terminateNonLeader, 1), dest = neighbors[0])
                    #comm.isend((rank, rndNum+1, 1, True, False, terminateNonLeader, 0), dest = neighbors[1])
                    numMessages+=1

                alreadyRecievedRight = True




