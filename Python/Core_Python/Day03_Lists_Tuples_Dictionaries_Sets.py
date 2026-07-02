# ==========================================
# Grrass Solutions - DSML Internship Program
# Author: Sujaan Bhalla
# ==========================================

print("Day 03 - Functions, Lists & Dictionaries")

# ==========================================
# Functions
# ==========================================

print("\n===== Functions =====")

def hello():
    print("Hello Function is Working")

hello()

# Function with Parameter
def greet(name):
    print("Welcome", name)

greet("Sujaan")

#Default Arguments

def add(a=2, b=3):
    print("Addition: ", a+b)

add(10,5)
add()

#Power Function

def power(a, b):
    print(a ** b)

power(5,2)
power(a=2, b=5)

#*args Example

def student(*a):
    print("Student Data:",a)
    print("First Value:", a[0])

student(1,2,3,4,5)

#Return Statement
def sum_numbers(a,b):
    return a+b

result = sum_numbers(10,20)
print("Result =", result)

# ==========================================
# Lambda Functions
# ==========================================

print("\n===== Lambda Functions =====")

add = lambda x,y:x + y
print(add(10,20))

square = lambda x,y:x*y
print(square(5))

numbers = lambda*x: [i for i in x]
print(numbers(10,20,30))

# ==========================================
# List Comprehension
# ==========================================

print("\n===== List Comprehension =====")

print([i for i in range(5)])

l = [10,20,30,40,50]

print([i for i in l])

nested = [ 10,20,[30,40,50,60]]

print([nested[2][i] for i in range(len(nested[2]))])

# ==========================================
# Lists
# ==========================================

print("\n===== Lists =====")
l = [10,20,30,40,50, "hello", True]
print(l)
print(l[0])
print(l[-1])

#append
fruits = ["Apple", "Banana"]
fruits.append("Mango")
print(fruits)

#insert
fruits.insert(1, "orange")
print(fruits)

#Nested List
data = [10,20,30,[40,50,[60,70,80]]]
print(data[3][2])

for i in data[3]:
    print(i)

# ==========================================
# Dictionaries
# ==========================================

print("\n===== Dictionaries =====")
student = {"name": "Sujaan", "age": 19, "course":"AI & DS"}
print(student)
print(student.keys())
print(student.values())

for key in student.keys():
    print("Key =", key)
    print("Value =", student[Key])

# ==========================================
# Nested Dictionary
# ==========================================

print("\n===== Nested Dictionary =====")
students = {
    "student1": {
        "name": "Sujaan",
        "age": 19
    },
    "student2": {
        "name": "Arya",
        "age": 20
    }
}

print(students)

for key, value in students.items():
    print(key, "=>", value)


# ==========================================
# My Practice
# ==========================================

print("\n===== My Practice =====")

def square_number(num):
    return num*num
print("Square =", square_number(10))

numbers = [10,20,30,40,50]
squares = [i**2 for i in numbers]
print("Squares =", squares)

print("\nDay 03 Completed Successfully!")