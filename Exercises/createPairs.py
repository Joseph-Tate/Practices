"""
createPairs.py is a python application that takes a single list and creates pairings that don't have the same pair listed twice, and won't have the same item from the list paired with
    itself.
Author: Joseph Tate
Version: 1.0
"""
import random
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

groups = createPairs(["Jo","Carolyne","Carly","Morgan","Matthew"])
for pair in groups:
    print(pair)
input("Press enter to exit")
