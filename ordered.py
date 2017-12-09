import instance_validator
import random
import sys
import math


#generates a series of constraints that points to two solutions
if (len(sys.argv) != 3):
    raise ValueError("must pass in filename and filesize")
filename = sys.argv[1]
filesize = sys.argv[2] #must be 20, 35 or 50
totalConstraints = (int(filesize) * (int(filesize) - 1)) / 2 - 1 #n(n-1)/2 - 1
extraConstaints = 0
if (totalConstraints > 500): #remove this if you want to see how many constraints would be generated without overflow handling
    extraConstaints = totalConstraints - 500

f = open(filename, 'r') #read
f.readline() #number of wizards
ordering = f.readline().strip("\n").split(" ") #optimal ordering
wizardSet = {} #set of wizard names
for i in range(len(ordering)):
    wizardSet[i] = ordering[i]
lower = 0
upper = len(wizardSet) - 1
f.close()


currentOrder = []
f = open(filename, 'a') #append
age1, age2, age3 = ordering[0:3] #initial 2 constraints with 3 variables to determine ordering 1 2 3 or 3 2 1
currentOrder += [age1, age2, age3]

f.write("{} {} {}\n".format(age1, age2, age3))
f.write("{} {} {}\n".format(age2, age3, age1))
numConstraints = 2

for i in range(3, len(ordering)):
    lower = 0
    upper = len(currentOrder) - 1
    nextElem = ordering[i]
    if (extraConstaints > 0): #we cannot place in every constraint, so we have to remove some
        #TODO: make this more random, instead of jumping 1, jump random amounts
        firstElem = currentOrder[0]
        secondElem = currentOrder[-1] #last element
        f.write("{} {} {}\n".format(firstElem, secondElem, nextElem))
        extraConstaints-= len(currentOrder) - 2 
        """ why len(currentOrder) - 2? Say I have abc, and I want to add d. 
        Using 3 constraints, I can narrow down abc/cba to abcd/dcba. Constraints are:
        a b d
        b c dcba
        d b a
        However, you can condense the constraints a b d and b c d to just a c d because 
        a c d provides as much information as the previous two statements
        Therefore, whenever we condense n-1 constraints to 1 constraint, we drop n-2 constraints."""
        numConstraints+=1
    else:
        for i in range(0, len(currentOrder) - 1): #iterate num elements - 1 times
            firstElem = currentOrder[i]
            secondElem = currentOrder[i+1]
            f.write("{} {} {}\n".format(firstElem, secondElem, nextElem))
            numConstraints+=1
    #last constraint must involve anything in order with nextElem in position 1 or 2
    secondIndex = random.randint(lower+1, upper) #cannot be the smallest element
    secondElem = currentOrder[secondIndex]
    thirdIndex = random.randint(lower, secondIndex - 1) #must be strictly smaller
    thirdElem = currentOrder[thirdIndex]
    f.write("{} {} {}\n".format(nextElem, secondElem, thirdElem))
    numConstraints+=1
    currentOrder += [nextElem]

#update number of constraints
f = open(filename, 'r')
arr = f.readlines()
f.close()

f = open(filename, 'w')
for i in range(len(arr)):
    if (i == 2):
        f.write(str(numConstraints) + "\n") #write in the correct number of constraints
    else:
        f.write(arr[i])

f.close()
x = instance_validator.main([filename, filesize]) 
print(x)


