# Booleans represent one of two values: True or False.
# When you compare two values, the expression is evaluated and Python returns the Boolean
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, Python returns True or False
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# Evaluate Values and Variables
# The bool() function allows you to evaluate any value
print(bool("Hello"))
print(bool(15))

# Evaluate two variables:
x = "Hello"
y = 15
print(bool(x))
print(bool(y))

# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.
print(bool(""))
print(bool(0))


# Functions can Return a Boolean
def myFunction():
    return True


print(myFunction())

# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
