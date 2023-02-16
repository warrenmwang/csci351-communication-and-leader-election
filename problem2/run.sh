#!/bin/bash
echo "problem 2 tests go here:"
echo "unidirectional LE ring test"
echo "" 
mpiexec -n 7 python unidirectionalLE.py --test ../tests/ringcopy.txt

echo "" 

python3 RandomRings.py --size 10
mpiexec -n 11 python unidirectionalLE.py --test ../tests/randomRing.txt

