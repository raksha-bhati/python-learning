#You can get the data type of any object by using the type() function:
x = 5
print(type(x))

#In Python, the data type is set when you assign a value to a variable:
#But, if you want to specify the data type, you can use the following constructor functions
x = str("Hello World")
x = int(20)
x = float(20.5)
x = complex(1j)
x = list(("apple", "banana", "cherry"))
x = tuple(("apple", "banana", "cherry"))
x = range(6)
x = dict(name="John", age=36)

#There are three numeric types in Python:
#float
#int
#complex
#Variables of numeric types are created when you assign a value to them:
x = 1    # int
y = 2.8  # float
z = 1j   # complex
print(x,y,z)

#You can convert from one type to another with the int(), float(), and complex() methods:
a = float(x)
b = int(y)
c = complex(x)
print(a,b,c)

#Random number
#Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:
#Import the random module, and display a random number between 1 and 9:
import random
print(random.randrange(1, 10))