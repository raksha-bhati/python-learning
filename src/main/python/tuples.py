# Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered and unchangeable.
thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuple items are ordered, unchangeable, and allow duplicate values.
# Ordered - When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Allows duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

# length of tuple
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item,
# otherwise Python will not recognize it as a tuple.
thistuple = ("apple",)
print(type(thistuple))

# not a tuple
thistuple = ("apple")
print(type(thistuple))

# Tuple items can be of any data type:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple can contain different data types:
tuple1 = ("abc", 34, True, 40, "male")

# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry"))  # note the double round-brackets
print(thistuple)

# You can access tuple items by referring to the index number, inside square brackets:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])

# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")

# Change tuple values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list,
# and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Add Items
# Once a tuple is created, you cannot add items to it.
# Workaround
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

# Remove Items
# Since , tuples are unchangeable
# Workaround
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

# Packing a tuple
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")  # packing a tuple

# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

# Using Asterisk*
# If the number of variables is less than the number of values, you can
# add an * to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

# If the asterix is added to another variable name than the last, Python will assign values to the
# variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)

# Multiply Tuples
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
