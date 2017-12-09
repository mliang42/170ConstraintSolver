import instance_validator
import random
import sys
import math


certainty = 20 #upper bound on the number of iteratiosn genWizards will run for each call. 
maxConstraints = 500
added = {}
def genWizards(wizardSet, lower, upper):
    i = 0
    while(True):
        i+=1
        wizard1 = wizardSet[random.randint(lower, upper)]
        wizard2 = wizardSet[random.randint(lower, upper)]
        wizard3 = wizardSet[random.randint(lower, upper)]
        #check if contained in added OR trivial
        string = wizard1 + wizard2 + wizard3
        string2 = wizard2 + wizard1 + wizard3 #equivalent order to string
        if (i >= certainty):
            #no more possible constraints left
            return string
        elif (string in added or string2 in added or wizard3 == wizard1 or wizard3 == wizard2 or wizard1 == wizard2):
            continue
        else:
            added[string] = 1
            return wizard1, wizard2, wizard3
    #return wizardSet[random.randint(lower, upper)],wizardSet[random.randint(lower, upper)],wizardSet[random.randint(lower, upper)]


#python bruteforce.py filename filesize
if (len(sys.argv) != 3):
    raise ValueError("must pass in filename and filesize")
filename = sys.argv[1]
filesize = sys.argv[2] #must be 20, 35 or 50

f = open(filename, 'r')
f.readline() #number of wizards
ordering = f.readline().strip("\n").split(" ") #perfect ordering
wizardSet = {} #set of wizard names
for i in range(len(ordering)):
    wizardSet[i] = ordering[i]
lower = 0
upper = len(wizardSet) - 1
f.close()

#update certainty value
certainty = int(math.factorial(len(wizardSet))/(math.factorial(3)*math.factorial(len(wizardSet)-3)))+ 1

while (True):
    x = instance_validator.main([filename, filesize])
    #print(x)
    if (x == "Success!"):
        f = open(filename, 'r')
        arr = f.readlines()
        #print(arr)
        #print(int(arr[2].strip("\n")))
        if (int(arr[2].strip("\n")) >= maxConstraints): 
            break
        arr[2] = (str(int(arr[2].strip("\n")) + 1) + "\n") #increase constraints by 1
        f.close()

        f = open(filename, 'w')
        #print(arr)
        for i in arr:
            if (i != "\n"):
                f.write(i)
        wizard1, wizard2, wizard3 = genWizards(wizardSet, lower, upper)
        f.write("{} {} {}\n".format(wizard1, wizard2, wizard3)) 
        f.close()
    else: 
        print(x)
        f = open(filename, 'r')
        arr = f.readlines()
        arr[2] = (str(int(arr[2].strip("\n")) - 1) + "\n")
        arr = arr[:-1] 
        #print(arr)
        f = open(filename, 'w')
        for i in arr:
            if (i != "\n"):
                f.write(i)
        f.close()
x = instance_validator.main([filename, filesize])
print(x)





