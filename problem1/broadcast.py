# broadcast from and convergecast to the root of a tree
# assume graph is a rooted tree

# mpiexec -n 11 python problem1.py
# w/ graphs.txt with 11 nodes [0, 10]
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

with open("../tests/graphs.txt", "r") as f:
    lines = f.readlines()
    tmp = lines[rank]
    tmp = tmp.split(":")
    tmp = tmp[1]
    tmp = tmp.split(",")
    neighbors = [int(x.strip()) for x in tmp]
    #print(f'rank {rank} has neighbors: {neighbors}')


# BROADCAST
# gonna use nonblocking send
if rank == 0:
    # root
    sendData = f"Hi from process {rank}"
    for i in neighbors:
        sendRequest = comm.isend(sendData, dest=i)
        #sendRequest.wait() 
    print(f"process {rank} terminating")
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
        sendRequest = comm.isend(sendData, dest=i)
        #sendRequest.wait()
    print(f"process {rank} terminating")

# CONVERGECAST
