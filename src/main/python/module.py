# Use a Module
# Now we can use the module we just created, by using the import statement:

# Import the module named mymodule, and call the greeting function:
import mymodule

mymodule.greeting("Jonathan")

# Variables in Module The module can contain functions, as already described, but also variables of all types (
# arrays, dictionaries, objects etc): Import the module named mymodule, and access the person1 dictionary:
a = mymodule.person1["age"]
print(a)

# Re-naming a Module
# #You can create an alias when you import a module, by using the as keyword:
import mymodule as mx

a = mx.person1["age"]
print(a)

# Built-in Modules
# There are several built-in modules in Python, which you can import whenever you like.
import platform

x = platform.system()
print(x)
x = dir(platform)
print(x)

# Note: When importing using the from keyword, do not use the module name when referring to elements in the module.
# Example: person1["age"], not mymodule.person1["age"]
