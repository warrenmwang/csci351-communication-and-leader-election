# broadcast from the root of a tree
# assume graph is a rooted tree
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

# BROADCAST
# gonna use nonblocking send
# you are root if your rank is in your neighbors list
if rank in neighbors:
    # root
    sendData = f"Root process {rank} sending broadcast."
    for i in neighbors:
        if rank != i:
            comm.isend(sendData, dest=i)
else:
    # non-root
    recvRequest = comm.irecv()
    while True:
        recvData = recvRequest.test()
        if recvData[0]:
            break
    print(f"process {rank} received: {recvData[1]}")
    for i in neighbors:
        comm.isend(recvData[1], dest=i)

