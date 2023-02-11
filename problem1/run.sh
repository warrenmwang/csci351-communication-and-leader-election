#!/bin/bash
echo "Broadcast test:"
mpiexec -n 15 python broadcast.py --test ../tests/rooted_tree0.txt
echo "" 
echo "Convergecast test:"
mpiexec -n 15 python convergecast.py --test ../tests/rooted_tree0.txt
