"""
Homework Assignment #4: Lists


Details:
 
Create a global variable called myUniqueList. It should be an empty list to start.

Next, create a function that allows you to add things to that list. Anything that's passed to this function should get added to myUniqueList, unless its value already exists in 
myUniqueList. If the value doesn't exist already, it should be added and the function should return True. If the value does exist, it should not be added, and the function should 
return False;

Finally, add some code below your function that tests it out. It should add a few different elements, showcasing the different scenarios, and then finally it should print the value 
of myUniqueList to show that it worked.


Extra Credit:

Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. If someone tries to add a value to myUniqueList but it's rejected 
(for non-uniqueness), it should get added to myLeftovers instead.


Submitted by: Jansen Gomez

"""

myUniqueList = []
myLeftovers =[]
listCount = 0

def AddToList(item):
    global listCount
    if listCount == 0:
        myUniqueList.append(item)
        listCount = 1
        return True

    elif listCount == 1:
        if myUniqueList[0] == item:
            return False
        else:
            myUniqueList.append(item)
            listCount = 2
            return True

    elif listCount == 2:
        if myUniqueList[0] == item:
            return False
        elif myUniqueList[1] == item:
            return False
        else:
            myUniqueList.append(item)
            listCount = 3
            return True

    elif listCount == 3:
        if myUniqueList[0] == item:
            return False
        elif myUniqueList[1] == item:
            return False
        elif myUniqueList[2] == item:
            return False       
        else:
            myUniqueList.append(item)
            listCount = 4
            return True
 

# Test Codes

# Add these values to the list
val1 = 1
val2 = 2
val3 = 3

listAdded = AddToList(val1)
print("listAdded = ", listAdded)
print("myUniqueList = ", myUniqueList[0])

listAdded = AddToList(val2)
if listAdded == False:
    myLeftovers.append(val2)
print("listAdded = ", listAdded)
print("myUniqueList = ", myUniqueList[0:2])
print("myLeftOvers = ", myLeftovers)

# Test if existing value will not be added
listAdded = AddToList(val2)
if listAdded == False:
    myLeftovers.append(val2)
print("listAdded = ", listAdded)
print("myUniqueList = ", myUniqueList[0:2])
print("myLeftOvers = ", myLeftovers[0])

# Continue adding unique value to list
listAdded = AddToList(val3)
if listAdded == False:
    myLeftovers.append(val3)
print("listAdded = ", listAdded)
print("myUniqueList = ", myUniqueList[0:3])
print("myLeftOvers = ", myLeftovers[0])

# Adding another non-unique value to list
listAdded = AddToList(val3)
if listAdded == False:
    myLeftovers.append(val3)
print("listAdded = ", listAdded)
print("myUniqueList = ", myUniqueList[0:3])
print("myLeftOvers = ", myLeftovers[0:2])