 ==========================================
#Grrass Solutions - DSML Internship Program
# Day 01 - Python Fundamentals
# Author: Sujaan Bhalla
# ==========================================

print("Welcome to Grrass Solutions - DSML Internship Program!")
print("Hello Sujaan!")

# ==========================================
# Variables
# ==========================================
a = 10
print("Value of a:", a)
print("Memory Address of a: ", id(a))

b = 10
print("Value of b:",b)
print("Memory Address of b:", id(b))

# ==========================================
# Data Types
# ==========================================
integer_num = 10
float_num = 10.5
string_name = "Python"
boolean_value = True

print( integer_num, type(integer_num))
print(float_num , type(float_num))
print(string_name, type(string_name))
print(boolean_value, type(boolean_value))

# ==========================================
# Input and Output
# ==========================================
name = input("Enter your name:")
print("Welcome", name)

num = input('enter a number:')
print("Original value:", num)
print("Data type:", type(num))

print('after integer conversion', int(num) +10)
print("String concatenation:" , num + str(10))
print("Repeated String: ", num * 5)

# ==========================================
# Type Conversion
# ==========================================
number = int(input("enter another number:"))
print(number)
print(type(number))

# ==========================================
# Arithmetic Operators
# ==========================================
a = 20
b = 5
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)

# ==========================================
# Even or Odd
# ==========================================

num = int(input("Enter a number: "))
print("the number you entered: ", num )

if num % 2 == 0:
    print(num, "is a even number.")
else:
    print(num, "is an odd number.")

# ==========================================
# Relational Operators
# ==========================================

x = 10
y = 20

print("equal to:" , x == y)
print("not equal to", x!=y)
print("Greater than", x>y)
print("less than", x<y)
print("greater than equal to" , x >= y)
print("less than equal to", x <= y)

# ==========================================
# Assignment Operators
# ==========================================

num = 10
num +=5
print("+=: ", num )
num -= 3
print("-= : ", num)
num *= 2
print("*= : ", num )
num /= 4
print("/= :", num)

# ==========================================
# Logical Operators
# ==========================================

a = True
b = False
print("AND: " a and b)
print("OR: ", a or b)
print("NOT:", not a)

# ==========================================
# My Practice Section
# ==========================================

college = "ACE Jaipur"
branch = "AI & DS "

print("\n ---Student Information---")
print("Name:", name)
print("College: ", college)
print("Branch: ", branch)

# eligibility to vote or not

if age>=18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

print("\n Day 01 Completed Successfully!")
