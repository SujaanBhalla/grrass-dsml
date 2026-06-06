# ==========================================
# #Grrass Solutions - DSML Internship Program
# Day 02 - Conditionals, Loops & Functions
# Author: Sujaan Bhalla
# ==========================================
print("Day 02 - Python Practice")
# ==========================================
# Logical Operators
# ==========================================
print(" \n ==== Logical Operators ==== ")

#and
num1 = 10
num2 = 20
print("AND:", num1 and num2)

# or
name1 = "hello"
name2 = ""

print("OR:", name1 or name2)
print("OR:", name2 or name1)

# not 
# list
data = []
print("NOT []:", not data)

#dictionary
data = {}
print("NOT {}:", not data)

# ==========================================
# Bitwise Operators
# ==========================================

print("\n===== Bitwise Operators =====")

a =5 #101
b =2 #010

#and 
print("a & b =", a & b) # 000
# or
print("a | b =", a | b)
#xor
print("a ^ b =", a ^ b)
#left shift
print("a << 1 =", a << 1)
#right shift
print("a >> 1 =", a >> 1)

# ==========================================
# Identity Operators
# ==========================================
print("\n===== Identity Operators =====")
list1 = [1,2,3]
list2 = [1,2,3]
list3 = list1

print("list1 == list2 :", list1 == list2)
print("list1 is list2 :", list1 is list2)
print("list1 is list3 :", list1 is list3)

print("Address list1:", id(list1))
print("Address list2:", id(list2))
print("Address list3:", id(list3))

# ==========================================
# Conditional Statements
# ==========================================

print("\n===== IF Statement =====")
num1 = 10
num2 = 20

if num1 < num2 :
    print("Greater Number:", num2)

# ------------------------------------------

print("\n===== IF ELSE =====")

number = int(input("Enter a number: "))

if number:
    print("Number entered:", number)
else:
    print("Number is zero")

# ------------------------------------------

print("\n===== IF ELIF ELSE =====")

age = int(input("Enter your age: "))

if age == 18:
    print("You are exactly 18 years old")
elif age > 18:
    print("You are above 18")
else:
    print("You are below 18")

# ==========================================
# FOR LOOP
# ==========================================

print("\n===== FOR LOOP =====")

for i in range(5):
    print(i)

# ------------------------------------------

print("\nNumbers 1 to 10")

for i in range(1, 11):
    print(i)

# ==========================================

print("\n===== LIST LOOP =====")
numbers = [11,12,13,14]

for item in numbers:
    print(item)

# ==========================================
# WHILE LOOP
# ==========================================

print("\n ===== WHILE LOOP =====")
i = 0
while i < 5:
    print(i)
    i += 1

# ==========================================
# BREAK
# ==========================================

print("\n===== BREAK =====")

for i in range(10):
    if i == 5:
        break
    print(i)

# ==========================================
# CONTINUE
# ==========================================

print("\n===== CONTINUE =====")

for i in range(6):
    if i == 3:
        continue
    print(i)

# ==========================================
# PASS
# ==========================================

print("\n===== PASS =====")

for i in range(5):
    if i == 2:
        pass
    print(i)

# ==========================================
# FUNCTIONS
# ==========================================

print("\n===== FUNCTIONS =====")

def greet():
    print("Hello Python")

greet()

# ------------------------------------------

def add(a,b):
    return a + b

result = add(10, 20)
print("Addition: ", result)

# ------------------------------------------

def numbers(*args):
    print("First Value:", args[0])

numbers(1,2,3,4)

# ==========================================
# My Practice
# ==========================================

print("\n ==== My Practice ====")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even number")
else:
    print("odd number")

print("\n Day 02 Completed Successfully!")
    

