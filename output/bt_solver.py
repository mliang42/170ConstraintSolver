import argparse
import sys
import random
import time
from random import shuffle

"""
======================================================================
  Complete the following function.
======================================================================
"""


def parse_constraints(wizards, constraints):
    cMap = dict()
    wizset = set(wizards)
    for constraint in constraints:
        for wiz in constraint:
            if (wiz not in wizset):
                return
            elif (wiz in cMap):
                cMap[wiz].append(constraint)
            else:
                cMap[wiz] = [constraint]
    return cMap

def solve(num_wizards, num_constraints, wizards, constraints):
    result = recursiveBackTracking([], constraints, wizards, set())
    #passes in initially empty assignment set
    return result

def recursiveBackTracking(assignment, constraints, wizards, assignment_set):
    for wizard in wizards:
        if (wizard in assignment_set):
            continue
        assignment.append(wizard)
        #print(assignment, flush = True)
        partial_constraints = findPartialContraints(assignment, cMap[wizard])

        if (len(assignment) < len(wizards) and validator(assignment, partial_constraints)):
            #runs the new assignment through the recursive backtracking algorithm if its valid
            result = recursiveBackTracking(assignment, constraints, wizards, set(assignment))
            if (len(result) == len(wizards) and validator(result, constraints)):
                #we have found a valid ordering
                return result
        if (len(assignment) == len(wizards) and validator(assignment, constraints)):
            #looks just like the statement above due to some poor logic
            return assignment
        assignment.pop()
    return [] #this case should never be called, unless there is no solution

def validator(lst, constraints): #return true or false
    #lst is a partial assignment which may or may not contain all wizards
    #constraints is a list of lists, where each constraint is a list
    for c in constraints: 
        wiz0 = c[0] 
        wiz1 = c[1]
        wiz2 = c[2]
        try:
            index0 = lst.index(wiz0)
        except ValueError:
            index0 = -1  #set to -1 if the wizard from the constraint is not in the partial assignment
        try:
            index1 = lst.index(wiz1)
        except ValueError:
            index1 = -1
        try:
            index2 = lst.index(wiz2)
        except ValueError:
            index2 = -1

        if ((index0, index1, index2).count(-1) == 1): #one item that is not in the list
            if ((index1 == -1 and index0 < index2) or (index0 == -1 and index1 < index2)):
                #doesn't work!
                #out of 6 possible orderings for some constraint a b c
                #if the lst has a c and b is not in there, then it fails
                #if the lst has b c and a is not in there, then it fails
                #other 4 options work
                #this is because we always add new wizards onto the end of the partial assignment
                return False
        elif (index0 < index2 < index1 or index1 < index2 < index0): #all three items in the constraint
            return False
        else:
            continue
    return True

def findPartialContraints(key, constraints):
    key = set(key)
    result = list()
    for constraint in constraints:
        count = 0
        for variable in constraint:
            if (variable in key):
                count+=1
        if (count == 2 or count == 3):
            result.append(constraint)
    return result


def specific_validator(num_wizards, num_constraints, output_lst, constraints):
    output_ordering_set = set(output_lst)
    output_ordering_map = {k: v for v, k in enumerate(output_lst)}

    constraints_satisfied = 0
    constraints_failed = []
    for i in range(num_constraints):
        constraint = constraints[i]

        c = constraint # Creating an alias for easy reference
        m = output_ordering_map # Creating an alias for easy reference

        wiz_a = m[c[0]]
        wiz_b = m[c[1]]
        wiz_mid = m[c[2]]

        if (wiz_a < wiz_mid < wiz_b) or (wiz_b < wiz_mid < wiz_a):
            constraints_failed.append(c)
        else:
            constraints_satisfied += 1

    return  constraints_failed, constraints_satisfied


"""
======================================================================
   No need to change any code below this line
======================================================================
"""

def read_input(filename):
    with open(filename) as f:
        num_wizards = int(f.readline())
        num_constraints = int(f.readline())
        constraints = []
        wizards = set()
        for _ in range(num_constraints):
            c = f.readline().split()
            constraints.append(c)
            for w in c:
                wizards.add(w)

    wizards = list(wizards)
    return num_wizards, num_constraints, wizards, constraints

def write_output(filename, solution):
    with open(filename, "w") as f:
        for wizard in solution:
            f.write("{0} ".format(wizard))

if __name__=="__main__":
    parser = argparse.ArgumentParser(description = "Constraint Solver.")
    parser.add_argument("input_file", type=str, help = "___.in")
    parser.add_argument("output_file", type=str, help = "___.out")
    args = parser.parse_args()


    start = time.clock()
    num_wizards, num_constraints, wizards, constraints = read_input(args.input_file)

    cMap = parse_constraints(wizards, constraints) #cMap maps each wizard to constraints involving it
    wizards.sort(key = lambda wizard: len(cMap[wizard])) #sort by number of constraints
    wizards = wizards[::-1] #reverse!
    #note: the above two lines are just an optimization
    solution = solve(num_wizards, num_constraints, wizards, constraints)
    print(solution)
    end = time.clock()
    print("Time spent in seconds = {}".format(end - start))
    
    constraints_failed, constraints_satisfied = specific_validator(num_wizards, num_constraints, solution, constraints)
    write_output(args.output_file, solution)
    
    