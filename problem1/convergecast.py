# convergecast the largest value to the root of the tree
# in our case, the message M_i will contain the id/rank of each process
# find the largest process ID
from mpi4py import MPI
import argparse
import sys
sys.path.insert(1, "..")
from utils import read_graph, is_leaf

parser = argparse.ArgumentParser()
parser.add_argument("--test", help="test file (graph in adjacency list form)")
args = parser.parse_args()
testfile = args.test

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

neighbors = read_graph(testfile, rank)


# CONVERGECAST
# parent is first id in neighbors
# you are root if first id is your id

# leaf
if is_leaf(neighbors, rank):
    # print(f"process {rank} is a leaf")
    # send M_i to parent
    sendData = rank
    parent = neighbors[0]
    comm.isend(sendData, dest=parent)
    # terminate
else:
    # non-leaf
    # Initially:
    vals = [rank]
    # Upon receiving a message
    while True:
        recvRequest = comm.irecv()
        while True:
            recvData = recvRequest.test()
            if recvData[0]:
                break
        x_j = recvData[1]
        print(f"process {rank} received {x_j=}")
        vals.append(x_j)
        if len(vals) == len(neighbors):
            x = max(vals)
            # send to parent if parent exists
            if neighbors[0] != rank:
                comm.isend(x, dest=neighbors[0])
            else:
                # you are the root
                print(f"Root of tree found max value: {x}")
            sys.exit()
