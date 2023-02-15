import sys

# reads the graph/rooted tree from testfile
# and for a process with rank rank calling this function, returns its neighbors
# parent process is first in list
def read_graph(testfile, rank):
    with open(testfile, "r") as f:
        lines = f.readlines()
        if len(lines) == 0:
            print("Empty file")
            sys.exit(0)
        tmp = lines[rank]
        tmp = tmp.split(":")
        tmp = tmp[1]
        tmp = tmp.split(",")
        neighbors = [int(x.strip()) for x in tmp]
    return neighbors

# returns true if the calling process with rank rank
# is a leaf process in its graph/tree
def is_leaf(neighbors, rank):
    if len(neighbors) == 1 and neighbors[0] != rank:
        return True
    else:
        return False
