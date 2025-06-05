#*************** For Loop Examples ****************#

#1: Iterating through a list
l = [1,2,3,4,5,6,7,8,9,0]
for i in l:
    print(i)

#2: Iterating through a string
s = "Manjiri"
for i in s:
    print(i)

#2 (Alternate): Iterating through a string directly
for i in "Manjiri":
    print(i)

#3: Iterating through a tuple
t = (1,2,3,4,5,6,7,8,9,0)
for i in t:
    print(i)

#4: Iterating through a mixed list
l1 = ["Manjiri", 456, 45+6j, 90.80]
for i in l1:
    print(i)

#*************** Data Type of Each Element ****************#

#1: Type of each element in a list
for i in l:
    print(type(i))

#2: Type of each character in a string
for i in s:
    print("Type of i:-", i, type(i))

#3: Type of each element in a tuple
for i in t:
    print(type(i))

#4: Type of each element in a mixed list
for i in l1:
    print(type(i))

#*************** Adding Number to Each Element ****************#

# Adding 2 to each number in a list
l2 = [1,2,3,4.5,6.77,8.9]
for i in l2:
    print(i + 2)

#*************** Storing Result in a New List ****************#

li = [1,2,3,4,5,6,7,8,9,0]
l3 = []
for i in li:
    print(i + 2)
    l3.append(i + 2)
    print(l3)

#*************** Extracting Specific Data Types ****************#

l4 = [1,2,3,3.4,4.5,6,7,8.9,9.0,6,7,"Manjiri",[45+6j]]
for i in l4:
    if type(i) == int:
        print(i)
    elif type(i) == list:
        print(i)

#*************** Getting Index of Elements ****************#

l5 = [1,2,3,4,5,6,7,8,9,0]
for i in l5:
    print("Index of element", i, "is:-", l5.index(i))

#*************** Extracting Strings and Characters ****************#

l6 = ["Manjiri",1,2,3,4,"Landge"]
l7 = []
for i in l6:
    if type(i) == str:
        print(i)
    elif type(i) == str:
        l7.append(i)
    elif type(i) == int:
        l7.append(i)
        print(l7)

# OR: For separating characters of string elements
for i in l6:
    if type(i) == str:
        l8 = []
        for j in i:
            l8.append(j)
            print(l8)

#*************** Square of Integer Elements ****************#

# Printing square of integers
l6 = ["Manjiri",1,2,3,4,"Landge",1,2,3,4]
for i in l6:
    if type(i) == int:
        print("Square of element", i, "is:-", i * i)
        i = i * i
        print(i)

# OR: Appending square of integers into a list
l9 = []
for i in l6:
    if type(i) == int:
        l9.append(i * i)
        print(l9)

#*************** Getting Index of All Elements ****************#

for i in range(len(l6)):
    print("Index of", i, "For an element:-", l6[i])

#*************** Using enumerate() ****************#

# Using enumerate to get index and value
for i in enumerate(l6):
    print(i)

# OR: Separate index and value
for i, j in enumerate(l6):
    print(i, j)

#*************** Using range() ****************#

# Demonstrating range and converting to list
print(range(4))
print(list(range(4)))
