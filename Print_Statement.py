# print(object, sep=' ', end='\n', file=sys.stdout, flush=False)
#Single Object
print("Hello World!")

# Multiple Objects
name = "Rahul"
age = 21
print("Name:", name, "Age:", age)

# Using "sep" (separation)
#Using Default Separator
print("Python", "is", "awesome")

#Custom Separator
print("2020", "10", "11", sep="-")

#Using "end"
#Default End
print("Hello")
print("World")

#Custom End
print("Python", end=" 🐍 ")
print("is fun!")

#Using ​​file
#Writing Output to a File
import sys                                      # Import sys module
file_output = open("output.txt", "w")           # Open a file in write mode
print("Hello from Python!", file=file_output)   # Print to the file instead of console
file_output.close()                             # Close the file

#Using flush
#Without Flush (Buffered Output)
import time
for i in range(3):
    print(i, end=' ')
time.sleep(1)

#With Flush=True
import time
for i in range(3):
    print(i, end=' ', flush=True)
time.sleep(1)