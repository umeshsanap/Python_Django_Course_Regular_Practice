#How to View Keywords in Python
import keyword
print(keyword.kwlist)

#how to write identifier
age = 20
print(age)

#valid identifier
name = "Umesh"
age_1 = 22
totalMarks = 480
_sum = 200
print(name, age_1, totalMarks, _sum)

#Invalid identifier
2name = "Raj"      #  Cannot start with a number
class = "A"        #  'class' is a keyword
my-name = "Ravi"   #  '-' is not allowed

#snake case identifier
student_marks = 90
print(student_marks)

#PascalCase identifier
class StudentInfo:
    pass

#Uppercase for constant
PI = 3.14159