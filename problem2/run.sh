#!/bin/bash
echo "problem 2 tests go here:"
echo "unidirectional LE ring test"
echo "" 
mpiexec -n 6 python unidirectionalLE.py --test ../tests/ringcopy.txt

