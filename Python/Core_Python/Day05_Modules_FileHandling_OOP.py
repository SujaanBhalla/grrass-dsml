# ==========================================
# Day 05 - Modules, File Handling & OOP
# Author: Sujaan Bhalla
# ==========================================
print("Day 05 - Python Practice")

# ==========================================
# Importing Modules
# ==========================================

print("\n===== Math Module =====")
import math

print("Factorial: ", math.factorial(5))
print("Power: ", math.pow(5,2))
print("Pi: ", math.pi)
print("Floor: ", math.floor(10.7234))
print("Ciel:", math.ciel(10.0123))

#Alias
import math as m 
print("\n Using Alias")
print(m.factorial(4))

#Specific Import
from math import factorial,pi
print("\n Specific Import")
print(factorial(6))
print(pi)

#Import All
from math import *
print("\n Import")
print(pow(5,3))
print(floor(10.3211))

# ==========================================
# File Handling
# ==========================================

print("\n===== File Handling =====")
file = open("sample.txt", "w")
file.write("Hello Sujaan \n")
file.write("Welcome to Python")
file.close()

file = open("sample.txt","r")
data = file.read()
print(data)
file.close()

# ==========================================
# Tuples
# ==========================================

print("\n===== Tuples =====")
t = (10,20,30,40)
print(t)
print(t[0])
print(t[-1])

# ==========================================
# Sets
# ==========================================

print("\n===== Sets =====")
s = {10,20,30,40,40,40}
print(s)
s.add(50)
print(s)

# ==========================================
# OOP - Class & Object
# ==========================================

print("\n===== Classes & Objects =====")

class Student:
    def __init__(self,name):
        self.name = name
    def show(self):
        print("Student Name:", self.name)

s1=Student("Sujaan")
s1.show()

# ==========================================
# Constructor Example
# ==========================================

print("\n===== Constructor Example =====")

class Person:

    def __init__(self,name):
        self.name = name

    def show(self):
        print("Constructor called")
    def display(self)
        print("Display Method")
p1= Person()
p1.display()

# ==========================================
# Class with Multiple Attributes
# ==========================================

print("\n===== Student Details =====")
class StudentInfo:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getName(self):
        print("Name: ", self.name)
    
    def getAge(self):
        print("Age:", self.age)
student = StudentInfo("Sujaan", 18)

student.getName()
student.getAge()

# ==========================================
# *args Example
# ==========================================

print("\n===== *args Example =====")
class Demo:
    def __init__(self,*args):
        self.data = args 
    def show(self):
        print(self.data)
d = Demo(10,20,30,40)
d.show()

# ==========================================
# **kwargs Example
# ==========================================

print("\n===== **kwargs Example =====")
def stu(**a):
    print(a)

stu(name="Sujaan", age = 19)

# ==========================================
# My Practice
# ==========================================

print("\n===== My Practice =====")

class College:
    def __init__(self,college_name, branch):
        self.college_name = college_name
        self.branch = branch
    
    def details(self):
        print("College:", self.college_name)
        print("Branch:",self.branch)

    c1 = college("ACE", "AI & DS")
    c1.details()
    
print("\nDay 05 Completed Successfully!")
