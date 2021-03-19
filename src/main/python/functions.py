# A function is a block of code which only runs when it is called.
# You can pass data, known as parameters, into a function.
# A function can return data as a result.

# Creating a function
def my_function():
    print("Hello from a function")


# Calling a function
my_function()


# Arguments
# Information can be passed into functions as arguments.
# Arguments are specified after the function name, inside the parentheses.
# You can add as many arguments as you want, just separate them with a comma.
def my_function(fname, lname):
    print(fname + " " + lname)


my_function("Emily", "Hayes")
my_function("Tobias", "Michale")
my_function("Linus", "Marvel")


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function,
# add a * before the parameter name in the function definition.
# This way the function will receive a tuple of arguments, and can access the items accordingly:
def my_function(*kids):
    print("The youngest child is " + kids[1])


my_function("Emil", "Tobias", "Linus")


# Keyword arguments
# You can also send arguments with the key = value syntax.
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function,
# add two asterisk: ** before the parameter name in the function definition.
# This way the function will receive a dictionary of arguments, and can access the items accordingly:
def my_function(**kid):
    print("His last name is " + kid["lname"])


my_function(fname="Tobias", lname="Refsnes")


# Default Parameter Value
# If we call the function without argument, it uses the default value:
def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry", 'orange']
my_function(fruits)


# Return Values from a function
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


# The pass Statement
# function definitions cannot be empty, but if you for some reason have a function definition with no content,
# put in the pass statement to avoid getting an error.
def myfunction():
    pass


# Recursion
# It means that a function calls itself.
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("\n\nRecursion Example Results")
tri_recursion(6)
