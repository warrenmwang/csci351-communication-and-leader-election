# CSCI351 Project 1: Communication and Leader Election
### Group: Joseph Carluccio, Yang Hong, Andrew Passero, Warren Wang

## File List

## Instructions
After cloning the repo, you may want to allow executable permissions to the bash scripts by running:
```
for f in $(find . -name *.sh); do chmod 700 $f; done
```
For each problem please run the `run.sh` file to run our tests against our programs:
Example for problem 1:
```
cd problem1 && ./run.sh && cd ..
```
If you want to run all the `run.sh` commands at once:
```
cd problem1 && ./run.sh && cd ../problem2 && ./run.sh && cd ../problem3 && ./run.sh && cd ../problem4 && ./run.sh && cd ..
```

Additionally for problem 2, issue the following command to run the message size simulation: 

```
cd problem2 && python3 simulateRings.py  
```

The results will be displayed in 'results.png' in the problem2 directory. 