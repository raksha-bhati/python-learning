import os

# Reading a text file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Writing to a new text file
with open('output.txt', 'w') as file:
    file.write("Hello, this is a sample output text.")

# appending to the above output file
with open('output.txt' , 'a') as file:
    file.write("\nHello, this is a sample output text 1.")

# reading from the above output file
with open('output.txt' , 'r') as file:
    content = file.read()
    print(content)

# deleting a file and checking if a file exists
if os.path.exists('output.txt'):
    os.remove('output.txt')
    print("file" , 'output.txt' , "deleted successfully")
else:
    print("file not found at this location")

# getting type of file
if os.path.isfile('example.txt'):
            _, file_extension = os.path.splitext('example.txt')
            print(file_extension.lower())


