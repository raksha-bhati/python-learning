# A Class is like an object constructor, or a "blueprint" for creating objects.

# Create a Class
class MyClass:
    x = 5


# Create Object
# Create an object named p1, and print the value of x:
p1 = MyClass()
print(p1.x)


# The __init__() Function
# All classes have a function called __init__(), which is always executed when the class is being initiated.
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)
print(p1.name, p1.age)


# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# Object Methods
# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


p1 = Person("John", 36)
p1.myfunc()


# Note: The self parameter is a reference to the current instance of the class,
# and is used to access variables that belong to the class.

# The self Parameter
# It does not have to be named self , you can call it whatever you like,
# but it has to be the first parameter of any function in the class:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)


p1 = Person("Jane", 36)
p1.age = 40
p1.myfunc()
print(p1.age)

# Delete Object properties
del p1.age

# Delete objects
del p1


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content,
# put in the pass statement to avoid getting an error.
class Person:
    pass
