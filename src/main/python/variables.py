"""Variables are containers for storing data values.
Python has no command for declaring a variable.
A variable is created the moment you first assign a value to it."""
x = 5
y = "John"
print(x, y)

# Variables do not need to be declared with any particular type,
# and can even change type after they have been set.
x = 4  # x is of type int
x = "Sally"  # x is now of type str
print(x)

# If you want to specify the data type of a variable, this can be done with casting.
x = str(3)  # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0
print(x, y, z)

# You can get the data type of a variable with the type() function.
x = 5.0
y = "John"
print(type(x))
print(type(y))

# String variables can be declared either by using single or double quotes:
x = "John"
# is the same as
x = 'John'
print(x)

# Variable names are case-sensitive.
a = 4
A = "Sally"
# A will not overwrite a
print(a, A)

# Python allows you to assign values to multiple variables in one line:
x, y, z = "Orange", "Banana", "Cherry"
print(x, y, z)

# And you can assign the same value to multiple variables in one line:
x = y = z = "Orange"
print(x, y, z)

#unpacking.
#If you have a collection of values in a list, tuple etc. Python allows you extract the values into variables.
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x,y,z)

#To combine both text and a variable, Python uses the + character
x = "awesome"
print("Python is " + x)

#You can also use the + character to add a variable to another variable
x = "Python is "
y = "awesome"
print(x+y)

#For numbers, the + character works as a mathematical operator:
x = 5
y = 10
print(x + y)

#Python does not combine a string and a number

#GLOBAL VARIABLES
#variables created outside of a function
#Global variables can be used by everyone, both inside of functions and outside.
x = "awesome"
def myfunc():
    print("Python is " + x)
myfunc()

#If you create a variable with the same name inside a function, this variable will be local,
# and can only be used inside the function. The global variable with the same name will remain as it was,
# global and with the original value.
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)

#To create a global variable inside a function, you can use the global keyword.
def myfunc():
 global x
 x = "fantastic"
myfunc()
print("Python is " + x)

#use the global keyword if you want to change a global variable inside a function.
x = "awesome"
def myfunc():
    global x
    x = "fantastic"
myfunc()
print("Python is " + x)