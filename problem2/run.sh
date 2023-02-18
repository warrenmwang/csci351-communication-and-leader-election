#!/bin/bash
echo ""
echo "problem 2 tests go here:"
echo "unidirectional LE ring test"
echo ""


echo "Running on ring1 with a size of 5 processes"
echo ""
mpiexec -n 6 python unidirectionalLE.py --test ../tests/ring1.txt
echo ""

echo "Running on ring1 with a size of 6 processes"
echo ""
mpiexec -n 7 python unidirectionalLE.py --test ../tests/ring2.txt
echo ""

echo "Running on randomly generate ring of size 10"
echo ""
python3 RandomRings.py --size 10
mpiexec -n 11 python unidirectionalLE.py --test ../tests/randomRing.txt
echo ""


echo "biidirectional LE ring test"
echo ""
echo "Running on ring1 with a size of 5 processes"
echo ""
mpiexec -n 6 python bidirectionalLE.py --test ../tests/ring1.txt
echo ""

echo "Running on ring1 with a size of 6 processes"
echo ""
mpiexec -n 7 python bidirectionalLE.py --test ../tests/ring2.txt
echo ""

echo "Running on randomly generate ring of size 10"
echo ""
python3 RandomRings.py --size 10
mpiexec -n 11 python bidirectionalLE.py --test ../tests/randomRing.txt
echo ""



