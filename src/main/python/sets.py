# A set is a collection which is both unordered and unindexed.
# Sets are unordered, so you cannot be sure in which order the items will appear.
myset = {"apple", "banana", "cherry"}
print(myset)

# Set items are unordered, unchangeable, and do not allow duplicate values.
# Sets are unchangeable, meaning that we cannot change the items after the set has been created.
# Once a set is created, you cannot change its items, but you can add new items.
# Duplicates Not Allowed

# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)

# Set() constructor
thisset = set(("apple", "banana", "cherry"))  # note the double round-brackets
print(thisset)

# You cannot access items in a set by referring to an index or a key.
# But you can loop through the set items using a for loop
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)

print("banana" in thisset)

# Add items
thisset.add("orange")
print(thisset)

# To add items from another set into the current set, use the update() method.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)

# If the item to remove does not exist, discard() will NOT raise an error.

# empties the set
thisset.clear()
print(thisset)

# Join 2 sets
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)

# Both union() and update() will exclude any duplicate items.

# Keep ONLY the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)

# The intersection() method will return a new set, that only contains the items that are present in both sets.
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)

# symmetric_difference_update() - Keep All, But NOT the Duplicates
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
