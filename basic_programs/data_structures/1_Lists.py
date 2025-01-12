# List is used to store multiple values in a single variable.
# List Items: Are ordered, changeable and allow duplicate values
# List items are indexed, the first item is at 0th index and the second is at [1]
# Ordered: Means items inserted in the list will maintain its order of insertion and will not change
# The insertion order can be change using different methods such as adding on to specific index of the list
# Any new item added will be placed the last of the list
# Changeable: Means we can add or remove the values after list is created
# Allows duplicate: Since list are indexed it can have duplicate values on different index

# EG

my_list = ["apple", "banana", "cherry", "kiwi", "sand", 25, False, 125]
print(my_list)

print(len(my_list))
print(type(my_list[6]))

# List constructor

thisList = list(("apple", "banana", "cherry"))
print(thisList)

# access the list
print(thisList[2])
print(thisList[-2])

# Specifying range of index

print(my_list[2:7])

print(my_list[3:len(my_list) - 1])

print("-------")
print(my_list[:3])

print(my_list[3:])

if "apple" in thisList:
    print("Yes apple is there")

for items in thisList:
    print(items)

fruits = ["apple", "banana", "cherry"]
# Change list items
fruits[1] = "Grapes"
print(fruits)

# Change range of items

fruits2 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
fruits2[1:5] = ["jack", "rock"]
print(fruits2)

# Insert item into list
fruits.insert(1, "Orange")
print(fruits)

# Append to the list
# Is used to all a new value to the end of the list

names = ["Rock", "Dan"]
names.append("Vivek")
print(names)

# Insert is used to insert a specific item to the list
names.insert(0, "FirstPerson")
print(names)

# Extend list
# To append elements from one list to another list use extend

list1 = ["Raj", "Ravi"]
list2 = ["Jaya", "Sushma"]
list1.extend(list2)
list1.extend(["Rekha", "Reema"])

print(list1)

# In order to add or append any iterable item you can use extend. Items such as tuple, dictionary or set to a list

listBase = ["a", "b"]
tuple1 = ("non-mutable", "tuple")
dictionary = {"key": "value1", "key2": "value2"}
set1 = {"set1", "Set2"}

listBase.extend(tuple1)
listBase.extend(dictionary.values())
listBase.extend(set1)

print(listBase)

# Remove items from the list

list3 = ["apple", "ball", "cat", "dog"]
if print(list3.remove("ball")) is None:
    print("This is the return of removal")
print(list3)

# Pop method, if index is not specified then it removed the last element of the list
print(list3.pop(0))  # return the value
print(list3)

# del keyword is also used to delete the elements from the list

del list3[0]
print(list3)

# Remove all the elements from the list

list3.clear()
print(list3)


print("----basic for loop----")
# Looping through the list

list4 = [10,20,30,40,50]
for a in list4:
    print(a)

print("----- for range ----")
# Looping through the index number

for i in range(len(list4)):
    print(list4[i])

print("_____While loop____")
# using while loop

i = 0
while i < len(list4):
    print(list4[i])
    i += 1

print("-----list comprehrnsion---")
# using list comprehension

[print(x) for x in list4]


