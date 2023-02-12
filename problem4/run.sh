#!/bin/bash
echo "Problem 4:"
echo "" && echo "AdaptedConvergecast tests:"
echo "" && echo "Using function max:"
mpiexec -n 15 python adapted_convergecast.py --test ../tests/rooted_tree0.txt --func max
echo "" 
mpiexec -n 11 python adapted_convergecast.py --test ../tests/rooted_tree1.txt --func max

echo "" && echo "Using function min:"
mpiexec -n 15 python adapted_convergecast.py --test ../tests/rooted_tree0.txt --func min
echo "" 
mpiexec -n 11 python adapted_convergecast.py --test ../tests/rooted_tree1.txt --func min

echo "" && echo "Using function sum:"
mpiexec -n 15 python adapted_convergecast.py --test ../tests/rooted_tree0.txt --func sum
echo "" 
mpiexec -n 11 python adapted_convergecast.py --test ../tests/rooted_tree1.txt --func sum

echo "" && echo "Using invalid functions:"
mpiexec -n 15 python adapted_convergecast.py --test ../tests/rooted_tree0.txt --func print
echo "" 
