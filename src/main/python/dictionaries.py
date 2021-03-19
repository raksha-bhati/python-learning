# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and does not allow duplicates.

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

# Dictionaries cannot have two items with the same key

# Length
print(len(thisdict))

# The values in dictionary items can be of any data type:
thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)

# You can access the items of a dictionary by referring to its key name
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict["model"])

# get() method - return value for key
print(thisdict.get("model"))

# keys() method will return a list of all the keys in the dictionary.
print(thisdict.keys())

# Add a new item to the original dictionary
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x)  # before the change
car["color"] = "white"  # add key and value to dict
print(x)  # after the change

# values() method - return a list of all the values in the dictionary.
print(thisdict.values())

# items() method will return each item in a dictionary, as tuples in a list.
print(thisdict.items())

# Check if Key Exists
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

# Change Values
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018
print(thisdict)

# update() method will update the dictionary with the items from the given argument.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)

# pop() method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

# popitem() method removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

# del keyword removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["brand"]
print(thisdict)

# del can also delete entire dict
del thisdict
# print(thisdict) #this will cause an error because "thisdict" no longer exists.

# clear() method empties dict
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

# loop through dict
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Print all key names
for x in thisdict:
    print(x)

# Print all values
for x in thisdict:
    print(thisdict[x])

# You can also use the values() method
for x in thisdict.values():
    print(x)

# Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)

# Copy a dict
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = thisdict.copy()
print(mydict)

# we can also use dict function
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
mydict = dict(thisdict)
print(mydict)

# Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}
print(myfamily)

child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print(myfamily)
