#============Explanation of Number data type with the program explanation============
#Integer
a = 10
b = -25
c = 0

print(a, type(a))
print(b, type(b))
print(c, type(c))

#float
x = 5.75
y = -2.3
z = 10.0
print(x, type(x))
print(y, type(y))
print(z, type(z))

#complex number
c = 2 + 3j
print(c)

#find real and imaginary part from the complex number
c = 2 + 3j
print(c)
print("Real part:", c.real)
print("Imaginary part:", c.imag)

a = 10
b = 3

#operations with number
print(a + b)   # Addition → 13
print(a - b)   # Subtraction → 7
print(a * b)   # Multiplication → 30
print(a / b)   # Division → 3.3333333333333335
print(a // b)  # Floor Division → 3
print(a % b)   # Modulus (Remainder) → 1
print(a ** b)  # Power → 1000

#type casting   
a = 5       # int
b = float(a)  # Convert to float
c = int(5.8)  # Convert to int (decimal part removed)
d = complex(a)  # Convert to complex

print(b, type(b))
print(c, type(c))
print(d, type(d))

#============Explanation of Number data type with the program explanation============
name = "Umesh"
message = 'Hello, World!'

print(name)
print(message)

#access character from string using index
word = "Python"
print(word[0])   # First letter
print(word[1])   # Second letter
print(word[-1])  # Last letter

#string slicing
text = "Programming"
print(text[0:6])   # From index 0 to 5 → 'Progra'
print(text[3:])    # From index 3 to end → 'gramming'
print(text[:5])    # From start to index 4 → 'Progr'

#string Concatenation
name1 = "Rahul"
name2 = "Jadhav"
print(name1 + name2)

#Repetition of string
greet = "Hello"
print(greet * 3)

#find number of character in string using len() function
msg = "Python"
print(len(msg))

#python can change the case using built-in function.
word = "python"
print(word.upper())   # PYTHON
print(word.lower())   # python
print(word.title())   # Python

#remove the space from starting and ending of the string.
text = "  Hello Python  "
print(text.strip())    # Removes spaces from both ends

#checking the content in string
name = "Python"
print(name.isalpha())   # True (only letters)
print(name.isdigit())   # False
print(name.startswith("P"))  # True
print(name.endswith("n"))    # True

#formating string
#1. using + operator
name = "Umesh"
age = 21
print("My name is " + name + " and I am " + str(age) + " years old.")

#2. using f string.
name = "Umesh"
age = 21
print(f"My name is {name} and I am {age} years old.")

# Syntax :- 
# my_list = [item1, item2, item3, ...]

# List of strings
fruits = ["apple", "banana", "cherry"]

# List of numbers
numbers = [10, 20, 30, 40]

# Mixed data types
mixed = [25, "hello", 9.8, True]

# Nested list (list inside a list)
matrix = [[1, 2, 3], [4, 5, 6]]

print(fruits)
print(numbers)
print(mixed)
print(matrix)

#Accessing the list element using indexing
fruits = ["apple", "banana", "cherry"]
print(fruits[0])   # apple
print(fruits[1])   # banana
print(fruits[-1])  # cherry (negative index = from end)

#Changin list item using indexing
num = [1,2,3,4,5]
num[0]="Aman"
print(num)

#Tuple
# Tuple creation
my_tuple = ("item1", "item2", "item3", ...)

# Tuple of strings
fruits = ("apple", "banana", "cherry")

# Tuple of numbers
numbers = (10, 20, 30, 40)

# Mixed data types
mixed = (25, "hello", 9.8, True)

# Nested tuple (tuple inside a tuple)
nested = ((1, 2, 3), (4, 5, 6))

print(fruits)
print(numbers)
print(mixed)
print(nested)

#Sets
# Creating a set
my_set = {"item1", "item2", "item3"}

# Normal set
fruits = {"apple", "banana", "cherry"}

# Duplicate items → automatically removed
numbers = {10, 20, 20, 30, 40, 10}

# Mixed data types
mixed = {25, "hello", 9.8, True}

print(fruits)
print(numbers)
print(mixed)

#frozen sets
nums = frozenset([1, 2, 3, 4])
# nums.add(5) ❌ Error (cannot modify)
print(nums)

# Dictionary
# Dictionary syntax
my_dict = {
    "key1": "value1", 
    "key2": "value2", 
    "key3": "value3"
    }

# Example of dictionary
student = {
    "name": "Ravi",
    "age": 22,
    "course": "Python",
    "marks": 90
}
print(student)

# 8788267372 --> Ganesh Shree Ram Lawns