# Legal variables names that can be declared
_my_var_1 = "Test_1"
my_var = "test3"
MY_VAR_2 = "ok"
OK = "test"

# Illegal variables

# 2_test = "invalid" cannot start with number or have space
# my var = "not valid"

# current value hold by an variable x= 4
x = "Sally"
print(x)
# here the latest value will be considered

# casting
name = "Vivek"
age = 32
# print( name + age) will throw error :TypeError: can only concatenate str (not "int") to str
print(name + "  " + str(age))

# Get the data type of variable
x = 3
y = "Sally"
my_list = [1, 2, 3]
print(type(x))
print(type(y))
print(type(my_list))

# Assign Many values to multiple variables

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# Assign multiple Variables to single value
a = b = c = "Universal"
print(a)
print(b)
print(c)

# Unpack Collection

fruits = ["apple", "banana", "Cheery"]
x, y, z = fruits

print(x)
print(y)
print(z)

# Output variables

x = "Python is Awesome"
print(x)

x = "Python"
y = "is"
z = "Awesome"
print(x, y, z)

x = "Python "
y = "is "
z = "Awesome"
print(x, y, z)

# NUMERIC concat : In case of numbers + operator will act as mathematical operator
x = 10
y = 90
print("This is concat", x + y)

x = 100
y = 900
print(f"This is addition {x + y}")

x = 10
y = 90
print("This is addition {}".format(x + y))

# GLOBAL variables : Variables declared outside the function is said to be global variables
# global variables can be used BOTH inside and outside the function

x = "Awesome"


def my_fun():
    print("This is called from inside function", x)


my_fun()


# Local variable when declared inside the function then its Local variable

def my_fun():
    x1 = "New Awesome"
    print("This is global variable", x)
    print("This is local variable", x1)


my_fun()

# In case you want to create a variable as global inside the function the use keyword as global

a_global = "first value"


def my_fun2():
    global a_global
    a_global = "This is new global value declared inside function"


my_fun2()
print(a_global)

# In the above case if we dont call the function then it wont get the global value declared inside the function

b_global = "Ranger value"


def my_fun3():
    global b_global
    b_global = "This is new global from b_global"


print(b_global)
# here this will print "Ranger value"
