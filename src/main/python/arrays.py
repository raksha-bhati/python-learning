# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.
# Arrays are used to store multiple values in one single variable:
cars = ["Ford", "Volvo", "BMW"]
print(cars)

# An array is a special variable, which can hold more than one value at a time.
# An array can hold many values under a single name, and you can access the values by referring to an index number.

# Access the Elements of an Array
print(cars[0])

# Modify the value of the first array item:
cars[0] = "Toyota"
print(cars)

# len()
print(len(cars))

# Looping Array Elements
for x in cars:
    print(x)

# Adding array elemensta
cars.append("Honda")
print(cars)

# Removing elements
cars.pop(1)
print(cars)

cars.remove("BMW")
print(cars)
