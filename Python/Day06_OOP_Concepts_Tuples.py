# ==========================================
# Day 06 - OOP Concepts & Tuples
# Author: Sujaan Bhalla
# ==========================================

print("Day 06 - OOP Concepts & Tuples")

# ==========================================
# Basic Class and Object
# ==========================================

print("\n===== Basic Class & Object =====")
class Address:
    city = "Jaipur"
    state = "Rajasthan"
a = Address()
print(a.city)
print(a.state)

# ==========================================
# Constructor
# ==========================================

print("\n===== Constructor =====")
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
a= Address("Jaipur", "Rajasthan")

print(a.city)
print(a.state)

# ==========================================
# Class Method and Self
# ==========================================

print("\n===== Class Method & Self =====")
class Address:
    def __init__(self, city, state):
        self.city = city
        self.state = state
    def show(self):
        print("The city is :", self.city)
a = Address("Jaipur", "Rajasthan")
a.show()

# ==========================================
# Inheritance
# ==========================================

print("\n===== Inheritance =====")
class Address:
    def __init__(self,city,state):
        self.city = city
        self.state = state
    def location(self):
        return f"My location is {self.city} in {self.state}"
class User(Address):
    def __init__(self, name, age, city, state):
        super().__init__(city, state)

        self.name = name
        self.age = age
    
    def userName(self):
        print(f"My name is {self.name}")

    def userDetails(self):
        print(f"My name is {self.name} and my location is {self.city} in {self.state}")
u = User("Sujaan", 18 , "Kukas", "Rajasthan")
print(u.city)
u.userDetails()
print(u.location())

# ==========================================
# Encapsulation
# ==========================================

print("\n===== Encapsulation =====")

class Address:
    def __init__(self,city,state):
        self.__city = city
        self.state = state
    
    def location(self):
        print(f"My location is {self.__city} in {self.state}")

    def getCity(self):
        return self.__city
a = Address("Chhapra", "Bihar")

a.location()
print(a.getCity())
print(a.state)

# ==========================================
# Polymorphism
# ==========================================

print("\n===== Polymorphism =====")

class Address:
    def __init__(self, city,state):
        self.city = city
        self.state = state

    def location(self):
        print(f"My address location is {self.city} in {self.state}")
    
class HomeTown:
    def __init__(self, city, state):
        self.city = city 
        sef.state = state
    
    def location(self):
        print(f"My hometown location is {self.city} in {self.state}")
a = Address("vadodara", "gujarat")
b = HomeTown("Chhapra","Bihar")
a.location()
b.location()

# ==========================================
# Class Variable
# ==========================================

print("\n===== Class Variable =====")
class Withdraw:
    total = 0
    def __init__(self, city , state):
        self.city = city
        self.state = state
        Withdraw.total += 1
a = Withdraw("Jaipur", "Rajasthan")
b = Withdraw("Bhilwara", "Rajasthan")
print("Total Objects:", Withdraw.total)

# ==========================================
# Method Overriding
# ==========================================

print("\n===== Method Overriding =====")

class Address:

    def location(self)
        print("Address Location")

class User(Address):

    def location(self):
        print("User Location")
u = User()
u.location()


# ==========================================
# Tuples
# ==========================================

print("\n===== Tuples =====")

marks = [ 98,45,45,34]
t = tuple(marks)
print(type(t))

m = list(t)
print(type(m))
print(m)

# ==========================================
# My Practice
# ==========================================

print("\n===== My Practice =====")

class College:

    def __init__(self, college, branch):
        self.college = college
        self.branch = branch
    def details(self):
        print("College:", self.college)
        print("Branch:", self.branch)

student = College("ACE", "AI & DS")

student.details()

print("\nDay 06 Completed Successfully!")
