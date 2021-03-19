# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

# Looping Through a String
# Even strings are iterable objects, they contain a sequence of characters:
for x in "banana":
    print(x)

# The break Statement
# With the break statement we can stop the loop before it has looped through all the items:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)

# The continue Statement
# With the continue statement we can stop the current iteration of the loop, and continue with the next:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)

# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function
# The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default),
# and ends at a specified number.
for x in range(6):
    print(x)
# Note that range(6) is not the values of 0 to 6, but the values 0 to 5.

# default range start from 0 but we can speicfy the range
for x in range(2, 6):
    print(x)

# he range() function defaults to increment the sequence by 1, however it is possible to specify the increment value
# by adding a third parameter: range(2, 30, 3):
for x in range(2, 30, 3):
    print(x)

# Else in For Loop
# The else keyword in a for loop specifies a block of code to be executed when the loop is finished:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# Note: The else block will NOT be executed if the loop is stopped by a break statement.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# Nested Loops
# A nested loop is a loop inside a loop.
# The "inner loop" will be executed one time for each iteration of the "outer loop"
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

# The pass Statement - for loop cannot be empty
for x in [0, 1, 2]:
    pass
