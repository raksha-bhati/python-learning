# Strings in python are surrounded by either single quotation marks, or double quotation marks.
print("Hello")

# Assign String to a Variable
a = "Hello"
print(a)

# You can assign a multiline string to a variable by using three quotes or single quotes:
# in the result, the line breaks are inserted at the same position as in the code.
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Strings are arrays
# strings in Python are arrays of bytes representing unicode characters.
# Square brackets can be used to access elements of the string.
a = "Hello, World!"
print(a[0])

# Looping Through a String
# Since strings are arrays, we can loop through the characters in a string, with a for loop.
for x in "banana":
    print(x)

# The len() function returns the length of a string:
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character is present in a string, we can use the keyword in.
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")

# To check if a certain phrase or character is NOT present in a string, we can use the keyword not in.
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

# Slicing
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.
b = "Hello, World!"
print(b[2:5])

# Slice From the Start
# By leaving out the start index, the range will start at the first character:
b = "Hello, World!"
print(b[:5])

# Slice To the End
# By leaving out the end index, the range will go to the end:
b = "Hello, World!"
print(b[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])

# Upper Case
a = "Hello, World!"
print(a.upper())

# Lower Case
print(a.lower())

# Remove Whitespace:Whitespace is the space before and/or after the actual text
# use strip() method
a = " Hello, World! "
print(a)
print(a.strip())  # returns "Hello, World!"

# Replace String
a = "Hello, World!"
print(a.replace("H", "J"))

# Split String
a = "Hello, World!"
print(a.split(","))  # returns ['Hello', ' World!']

# String Concatenation
# To concatenate, or combine, two strings you can use the + operator.
a = "Hello"
b = "World"
print(a + " " + b)

# String format
# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are:
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# Escape Character(\)
txt = "We are the so-called \"Vikings\" from the north."
print(txt)

# escape characters in python
# \'	Single Quote
# \\	Backslash
# \n	New Line
# \r	Carriage Return
# \t	Tab
# \b	Backspace
# \f	Form Feed
# \ooo	Octal value
# \xhh	Hex value

# String Methods
# Python has a set of built-in methods that you can use on strings.
# All string methods returns new values. They do not change the original string.
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	    Returns a centered string
# count()	    Returns the number of times a specified value occurs in a string
# encode()	    Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	    Searches the string for a specified value and returns the position of where it was found
# format()	    Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	    Searches the string for a specified value and returns the position of where it was found
# isalnum()	    Returns True if all characters in the string are alphanumeric
# isalpha()	    Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	    Returns True if all characters in the string are digits
# isidentifier()Returns True if the string is an identifier
# islower()	    Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	    Returns True if all characters in the string are whitespaces
# istitle()	    Returns True if the string follows the rules of a title
# isupper()	    Returns True if all characters in the string are upper case
# join()	    Joins the elements of an iterable to the end of the string
# ljust()	    Returns a left justified version of the string
# lower()	    Converts a string into lower case
# lstrip()	    Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	    Returns a string where a specified value is replaced with a specified value
# rfind()	    Searches the string for a specified value and returns the last position of where it was found
# rindex()	    Searches the string for a specified value and returns the last position of where it was found
# rjust()	    Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	    Splits the string at the specified separator, and returns a list
# rstrip()	    Returns a right trim version of the string
# split()	    Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	    Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	    Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	    Converts a string into upper case
# zfill()	    Fills the string with a specified number of 0 values at the beginning
