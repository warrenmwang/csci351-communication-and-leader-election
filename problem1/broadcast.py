# broadcast from the root of a tree
# assume graph is a rooted tree
from mpi4py import MPI
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--test", help="test file (graph in adjacency list form)")
args = parser.parse_args()
testfile = args.test

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

with open(testfile, "r") as f:
    lines = f.readlines()
    tmp = lines[rank]
    tmp = tmp.split(":")
    tmp = tmp[1]
    tmp = tmp.split(",")
    neighbors = [int(x.strip()) for x in tmp]

# BROADCAST
# gonna use nonblocking send
# you are root if your rank is in your neighbors list
if rank in neighbors:
    # root
    sendData = f"Hi from process {rank}"
    for i in neighbors:
        if rank != i:
            comm.isend(sendData, dest=i)
    # print(f"process {rank} terminating")
else:
    # non-root
    recvRequest = comm.irecv()
    while True:
        recvData = recvRequest.test()
        if recvData[0]:
            break
    print(f"process {rank} received a msg: {recvData[1]}")
    sendData = f"Hi from process {rank}"
    for i in neighbors:
        comm.isend(sendData, dest=i)
    # print(f"process {rank} terminating")

