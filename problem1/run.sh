#!/bin/bash
echo "Problem 1:"
echo "Broadcast tests:"
mpiexec -n 15 python broadcast.py --test ../tests/rooted_tree0.txt
echo "" 
mpiexec -n 11 python broadcast.py --test ../tests/rooted_tree1.txt
echo ""
echo "testing on empty tree:"
mpiexec -n 10 python broadcast.py --test ../tests/empty_graph.txt

echo "" && echo "Convergecast tests:"
mpiexec -n 15 python convergecast.py --test ../tests/rooted_tree0.txt
echo "" 
mpiexec -n 11 python convergecast.py --test ../tests/rooted_tree1.txt
echo ""
echo "testing on empty tree:"
mpiexec -n 10 python broadcast.py --test ../tests/empty_graph.txt
