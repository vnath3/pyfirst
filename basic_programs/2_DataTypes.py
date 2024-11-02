import random
import random as ra


# Built-in data types

# Text type : str
# Numeric types: int, float, complex
# Sequence types list, tuple, range
# Mapping types : dict
# Set types: set, frozenset
# Boolean bool
# Binary types : bytes, bytearray, memory view
# None type: NoneType


# Getting data type

x = "This is string"
print(type(x))

# Numbers
x = 1
y = 2.8
z = 1j
print(type(x))
print(type(y))
print(type(z))

# Type conversion

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
c = complex(x)

print(a)
print(b)
print(c)

# in case of round off :

x = 2.8

d = int(round(x))
print(d)

print("------------------------")

print(ra.randrange(1, 10))
print(random.randrange(1, 10))
