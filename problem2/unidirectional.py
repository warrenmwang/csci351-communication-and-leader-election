#TODO: implement and test the unidirectional and bidirectional (tournament-style) Leader
# Election algorithms for asynchronous rings
from mpi4py import MPI
import argparse
import sys
sys.path.insert(1, "..")
from utils import read_graph

parser = argparse.ArgumentParser()
parser.add_argument("--test", help="test file (graph in adjacency list form)")
args = parser.parse_args()
testfile = args.test

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# get neighbors
neighbors = read_graph(testfile, rank)

#unidirectional algorithm
#initially
sendData = rank
comm.isend(sendData, dest = leftNeighbor)
#receiving
while True:
        recvRequest = comm.irecv()
        recvData = recvRequest
        #if x is not i and x > i
        if recvData != rank and recvData > rank:
            #send recvRequest to left neighbor
            sendData = recvRequest
            comm.isend(sendData, dest = leftNeighbor)
        #if x = i
         Leader = 
            


