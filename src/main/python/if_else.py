# IF
a = 33
b = 200
if b > a:
    print("b is greater than a")

# Elif
# If the previous conditions were not true, then try this condition
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")

# Else
# else keyword catches anything which isn't caught by the preceding conditions.
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")

# Short Hand If - Ternary Operators, or Conditional Expressions.
if a > b: print("a is greater than b")

# Short Hand If ... Else - Ternary Operators, or Conditional Expressions.
a = 2
b = 330
print("A") if a > b else print("B")

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# And
# The and keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")

# Or
# The or keyword is a logical operator, and is used to combine conditional statements:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")

# Nested If
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")

# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content,
# put in the pass statement to avoid getting an error.
a = 33
b = 200
if b > a:
    pass
