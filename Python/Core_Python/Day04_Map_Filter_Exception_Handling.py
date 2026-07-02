# ==========================================
# Day 04 - Map, Filter & Exception Handling
# Author: Sujaan Bhalla
# ==========================================

print("Day 04 - Python Practice")

# ==========================================
# Nested Lists & Slicing
# ==========================================

print("\n===== Nested Lists =====")

l = [10,20,30, ["hello","hello1","hello3", [True, False]]]
print(l)
print(l[-1])
print(l[-1][0])
print(l[-1][-1])

print("\n===== Slicing =====")

numbers = [10,20,30,40,50]
print(numbers[:3])
print(numbers[2:])
print(numbers[::-1])

# ==========================================
# Dictionary Methods
# ==========================================
print("\n ===== Dictionary Methods =====")

student = {
    "name": "Sujaan", 
    "age": 18,
    "course": "AI & DS"}
print(student.get("name"))
print(student.keys())
print(student.values())
print(student.items())

student.update({"city": "Jaipur"})
print(student)

copy_dict = student.copy()
print(copy_dict)

# ==========================================
# Map Function
# ==========================================

print("\n===== Map Function =====")

numbers = [10,20,30]
square = list(map(lambda x:x*x, numbers))
print(square)

# ==========================================
# Filter Function
# ==========================================

print("\n===== Filter Function =====")
def check_word(word):
    return word.endwith("a")

words = ["apple", "banana","cat","dog"]
result = list(filter(check_word,word))
print(result)

# ==========================================
# Reduce Function
# ==========================================

print("\n ==== Reduce Function ====")
from functools import reduce
numbers = [10,20,30,40]
result = reduce(lambda x,y: x+y , numbers)
print(result)

# ==========================================
# Exception Handling
# ==========================================

print("\n===== Try Except =====")
try:
    num1 = 10
    num2 = 5
    print(num1 / num2 )
except:
    print("Error occured")

# ------------------------------------------

print("Division by zero")

try:
    num1 = 10
    num2 = 0
    print(num1/num2)
except:
    print("Denominator can't be zero")

# ------------------------------------------

print("\n===== Try Except Finally =====")
try:
    num1 = 20
    num2 = 4
    print(num1/num2)
except:
    print("Error")
finally:
    print("Finally Block Executed")

    # ==========================================
# My Practice
# ==========================================

print("\n===== My Practice =====")
try:
    age = int(input("Enter your age: "))
    print("Your Age:", age)
except:
    print("Please enter a valid number")

finally:
    print("Program Completed")
print("\nDay 04 Completed Successfully!")
