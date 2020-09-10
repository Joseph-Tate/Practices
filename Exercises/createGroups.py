"""
createGroups.py is a python application that takes a single list and creates pairings based on a set of rules. The user will have the ability to add any lists and rules that they desire.
Author: Joseph Tate
Version: 1.0
"""
#imports
import random

#crearePairs
def createPairs(lst):
    random.shuffle(lst)
    lst2 = []
    exclude = []
    for i in range(len(lst)):
        # Gets an index value from lst1 that isnt already used in lst2 or matches lst1 at that index
        val = random.choice([j for j in range(len(lst))
                             if j not in exclude and j != i])
        # Appends lst1[val] to lst2 and val to exclude
        lst2.append(lst[val])
        exclude.append(val)
    # Returns the pairings
    return list(zip(lst, lst2))

#printGroup
def printGroup(group):
    for pair in group:
        print(pair)

for iter in range(5):
    printGroup(createPairs(["Matthew","Morgan","Carly","Joseph","Dad"]))
