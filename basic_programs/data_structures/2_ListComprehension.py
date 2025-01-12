# List comprehension offers a short syntax when you want to create a new list based on the values of an existing list

# Example using fruits list you want to create a list of fruits having a letter in it the it can used

# Without this will have to iterate using for and insrt the elements matching condition

# Without comprehension
fruits = ["apple", "banana", "coconut", "dates", "Grapes"]
newList = []
for x in fruits:
    if "c" in x:
        newList.append(x)

print(newList)

# With comprehension

newList2 = [x for x in fruits if "c" in x]
print(newList2)

# its: [expression for item in iterable if condition]
# expression: item to include in the new list x in this case
# for item in iterable: iterates over each item in the list or sequence (fruits in this case)
# if condition: Optional a condition to filter which items are to be included in the new list in this case newList2
# List comprehension provides a concise way to filter and transform the data in a list
# These are more readable and efficient
# Returned value is a new list, leaving the old list unchanged


# Without if condition it will simply create a new empty list
newList3 = [fruit for fruit in fruits]
print(newList3)

# can use range as well
newlist5 = [x for x in range(10)]
print(newlist5)


