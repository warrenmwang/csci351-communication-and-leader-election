#TODO: implement broadcast from and convergecast to the root of a tree
# assume graph is a rooted tree
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print(rank)
