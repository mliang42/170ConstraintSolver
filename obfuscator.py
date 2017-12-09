import instance_validator
import random
import sys
import math

filename = sys.argv[1]
filesize = sys.argv[2]
#assume wellformed input
f = open(filename, 'r')
arr = f.readlines()
print("number of rows = {}".format(len(arr)))
f.close()

#TODO: replace all wizards with random 10 character strings
f = open(filename, 'r') #read
numWizards = f.readline() #number of wizards
ordering = f.readline().strip("\n").split(" ") #optimal ordering
wizardSet = {} #set of wizard names
for i in range(1, len(ordering)+1):
    randomInt = random.randint(0, 1000000000)
    while(randomInt in wizardSet.values()):
        randomInt = random.randint(0, 1000000000)
    wizardSet[i] = randomInt #ordering[i]
print(wizardSet)
print("_---------------")
for i in range(len(arr)):
    if (i == 1 or i >=3):
        lst = arr[i].strip("\n").split(" ")
        print(lst)
        string = ""
        for val in lst:
            string += str(wizardSet[int(val)]) + " "
        string = string[:-1]
        arr[i] = string + "\n"
print(arr)
f.close()

f = open(filename, 'w')
for line in arr:
    f.write(line)
f.close()

print("number of rows = {}".format(len(arr)))

hashset = set()
for i in range(len(arr)):
    if (i < 3): #ignore first 3 lines
        continue
    else:
        #Collisions
        hashset.add(arr[i]) #stores constraints
        

print("len of hash is ={}".format(len(hashset)))

f = open(filename, 'w')
for i in range(3):
    if (i == 2):
        f.write(str(len(hashset)) + "\n")
    else:
        f.write(arr[i]) #write back header part consisting of numWizards, optimal ordering, and numConstraints
for constraint in hashset: #supposedly unordered
    #TODO:can possible rearrange wizard 1 and 2 in the constraint randomly
    f.write(constraint)
f.close()
x = instance_validator.main([filename, filesize]) 
print(x)

