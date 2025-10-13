# 'age' is a variable storing an integer value
age = 21  

# Now the box has text "Hello"
box = "Hello"  

#Local Variable declaration
def greet():
    message = "Hello, World!"   # Local variable
    print(message)

greet()

#Global Variable Declaration
name = "Umesh"          # Global variable
def show_name():
    print("Inside function:", name)
show_name()
print("Outside function:", name)

#We can update global variable using global keyword
count = 0

def increment():
    global count
    count += 1

increment()
print(count)  # Output: 1

#Instance Variable
class Student:
    def __init__(self, name, age):
        self.name = name      # Instance variable
        self.age = age        # Instance variable

s1 = Student("Ravi", 22)
s2 = Student("Priya", 21)

print(s1.name, s1.age)   # Ravi 22
print(s2.name, s2.age)   # Priya 21

#Class variable
class Employee:
    company = "TechCorp"   # Class variable (shared)

    def __init__(self, name):
        self.name = name   # Instance variable (unique)

e1 = Employee("Amit")
e2 = Employee("Neha")

print(e1.company)  # TechCorp
print(e2.company)  # TechCorp

# Changing class variable (affects all objects)
Employee.company = "NextGenTech"

print(e1.company)  # NextGenTech
print(e2.company)  # NextGenTech

#decaration of simple variables
name = "Umesh"   # String variable
age = 21         # Integer variable
height = 5.8     # Float variable
is_student = True  # Boolean variable

print(name, age, height, is_student)

#change the variable value into the same program
box = 10
print(box)   # 10

box = "Hello"
print(box)   # Hello


#Assigning multiple values to the multiple variable simultaneously.
a, b, c = 5, 10, 15
print(a, b, c)

#Used variable in expression, print variable value using comma.
x = 10
y = 5
sum = x + y
product = x * y
print("Sum:", sum)
print("Product:", product)

#Variable swapping in pythonnic way
a = 5
b = 10
a, b = b, a
print("a =", a, "b =", b)