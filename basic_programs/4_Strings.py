# Quotes inside quotes

x = "This is too 'hard'"
y = 'This is too "easy"'

print(x)
print(y)

# Use tripe  quotes to define multi-line statements
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(x)
print("---------------------------")

# String as an array

x = "This is String"
print(x[0])

# looping through string

for value in x:
    print(value)

for value in "Banana":
    print(value)

# String length

print(len(x))
print("------------------")
# Check value is present in string or not

x = "This is the world"

if "world" in x:
    print("Yes world is there")

print("world" in x)

# Use not

if "unknown" not in x:
    print("Word is missing")

print("World" not in x)

print("------------------")

# To get a range of characters by using the slice syntax

# Range
x = "This is new era"
print(x[3:8])

# From Start
print(x[:5])

# Till end
print(x[0:])

# Negative indexing
b = "Hello, World!"
print(b[-5:-2])

# equivalent in positive
print(b[8:11])

c = "abcdefghijk"
print(c[3:5])
# def or de ? So it doesnt get the last character i.e. var[startIndex : endIndex-1]


# Modify a string using methods

# Upper case

a = "Hello, World.!  "
print(a.upper())

# Lower case
print(a.lower())

# Remove white spaces
print(a.strip())

# Replace string

print(a.replace("H", "XX"))

# Split
print(a.split(","))
print(a.split(",")[0])

# Concatenate String
# in order to join two string use + operator

a = "Born"
b = "King"
c = a + b
print(c)

print(a + " " + b)

print("------------------")

# Format string
age = 32
# print("This is my age " + age) this will give exception that TypeError: can only concatenate str (not "int") to str
# F-strings Was introduced in py 3.6 and is NOW a Preferred way of formatting string to specify a string as an f-string
# simply put an f in front of the string literal and add curly brackets {} as placeholder for variables and other
# operations.

print(f"This is my age {age}")
my_list = ["orange", "mangoes", "apple"]

print(f"The fruits i have are {my_list}")

pi = 3.143

print(f"The value of pi is {pi}")

# Placeholder

rate = 85

print(f"I spent {rate * 32} dollars ")

# Adding a modifier, it is included by adding a : "colon" followed by legal formatting type like .2f which means
# fixed point number with 2 decimals

print(f" I spent {rate*32:.2f} when was in US")

print("------------------")

# Escape characters

# To insert characters that are illegal in a string, use escape character.
# An escape character is a backslash \ followed by the character you want to insert
# An example of an illegal character is Double quotes inside a string that is surrounded by double quotes:
# txt = "We are the "Gods" now"
# fix is as is use escape characters

txt = " We are the \"Gods\" now "
print(txt)

# new line
print("This is first line \n This is second line \n This is third ")

# Tab
print("After tab \t text will have a tab")



