# String methods

x = " Guns in head AND they wont go."

# Converts the first character to upper case or lower case
print(f"Capitalize = {x.capitalize()}")

# Method will align the string using a specified characters, space is default
print(x.center(300))
print(x.center(200, "#"))

# Converts Complete string into upper case
print(f"Upper = {x.upper()}")

# Converts string into lower case
print(f"Case-fold = {x.casefold()}")

# Converts the complete string into lower case
print(f"Lower = {x.lower()}")

# So in the above both case-fold and lower have similar output so what's the difference lower is light version,
# can be used when you are sure that language specific characters aren't a concern Case-fold use when performing
# case-insensitive string comparisons or when working with multilingual text that might include special characters EG
# "FUN!".lower() = fun! Eg Straße.casefold() = strasse

text = "Straße"
print(text.lower())    # Output: "straße" (standard lowercase conversion)
print(text.casefold()) # Output: "strasse" (handles special case folding)


a = "this is this repeat the word this and this is fine"
print(f"count word this = {a.count("this")}")
print(f"count with range : {a.count("this", 5, 30)}")

txt1 = "My name is Ståle"
print(txt1.encode())


# ends with
print(f"Ends with \"fine\" {a.endswith("fine")}")


# Find methods
# Finds the first occurrence of string and returns 0 if found else -1
# same as index method, but it does not raise an exception when value is not found
txt2 = "World will be mine"
print(f"Find action {txt2.find("World")}")
print(f"Find action {txt2.find("unknown")}")
try:
    print(f"Index matched {txt2.index("World")}")
    print(f"Index not matched {txt2.index("Z")}")
except ValueError as e:
    print(f"Exception occurred : {e}")


# Format
#  method formats the specified values amd insert them inside the string placeholder
#  is defined by curly braces {}.
# Format method returns a formatted string


txt3 = "I spent {price:.2f} dollars.!"
print(txt3.format(price=20))

txt4 = "My name is {0} and age is {1}"
print(txt4.format("Vivek", 32))

txt5 = "My location is {} and i work from {}"
print(txt5.format("Pune", "Home"))


# Format map
# is used to format a string using dictionary as the source of values for named placeholders.
data = {"name": "Alice", "age": 25, "city": "New York"}

format_string = "Name={name}, Age:{age}, City:{city}".format_map(data)
print(format_string)
print(data.get("name"))


x = "This2isAlpg"
print(x.isalnum())
print(x.isalpha())
x = "123"
y = "ONE"
print(x.isdigit())
print(y.isdigit())


# Join
# Used to join all the items from tuple into a string
# tuple is a type of data structure used in py
# Def join takes all items in an iterable and joins into one string

myTuple = ("Jane", "John", "Adam", "Ada")

x = "__".join(myTuple)
print(f"After join =  {x}")


# Similarly, we can join keys from the dictionary

myDict = {"name": "Rock", "county": "India", "age": 40, "isActive": True}

mySeperator = "$$"
x = mySeperator.join(myDict)
print(f"Join dictionary = {x}")


# Lstrip strips only from left where as strip strips from both ends


text = "!!!Hello, World!!!"

print(text.lstrip("!"))  # Output: "Hello, World!!!"
print(text.strip("!"))   # Output: "Hello, World"


# Partition: will return a tuple with three elements. 1- everything before match, 2- the match and 3- everything
# after the match

txt7 = "I could eat bananas all day"
print(txt7.partition("bananas"))

# in case of unmatched string

print(f"Unmatched = {txt7.partition("apples")}")

# Replace : use to replace a string

txt8 = " I am Good !! "
print(txt8.strip().replace("Good", "Great"))


# rfind() returns the index of matched string.
# If not found will return -1
# Almost similar to rindex

txt9 = "Make it larger than life"
print(txt9.rfind("life"))
print(txt9.rfind("it"))
print(txt9.rindex("it"))

print(txt9.rfind("ok"))

# with range of index to search

print(txt9.rfind("t",3,9))


# Get length of string
txt10 = "OkWorld"
print(len(txt10))