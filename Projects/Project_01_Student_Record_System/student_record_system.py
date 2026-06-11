# ==========================================================
# GRRAS Solutions
# Author : Sujaan Bhalla
# Project 01 : Student Record Management System
# Description :
# A simple OOP-based student management system that
# allows users to Add, Search, Update, Delete and
# View student records.
# ==========================================================


# ==========================================================
# Student Manager Class
# ==========================================================

class StudentManager:

    # Constructor
    def __init__(self):

        # List to store student records
        self.students = []


    # ======================================================
    # Add Student
    # ======================================================
    def add_student(self):

        print("\n----- Add Student -----")

        name = input("Enter Student Name : ")
        age = int(input("Enter Student Age : "))
        city = input("Enter Student City : ")

        student = {
            "name": name,
            "age": age,
            "city": city
        }

        self.students.append(student)

        print("\n  Student Added Successfully")


    # ======================================================
    # Show All Students
    # ======================================================
    def show_students(self):

        print("\n----- Student Records -----")

        if len(self.students) == 0:
            print("No Student Records Found")
            return

        for student in self.students:
            print(student)


    # ======================================================
    # Search Student
    # ======================================================
    def search_student(self):

        print("\n----- Search Student -----")

        name = input("Enter Student Name : ")

        for student in self.students:

            if student["name"].lower() == name.lower():

                print("\nStudent Found")
                print(student)

                return

        print("\n Student Not Found")


    # ======================================================
    # Update Student
    # ======================================================
    def update_student(self):

        print("\n----- Update Student -----")

        name = input("Enter Student Name : ")

        for student in self.students:

            if student["name"].lower() == name.lower():

                new_city = input("Enter New City : ")

                student["city"] = new_city

                print("\n Student Updated Successfully")

                return

        print("\n Student Not Found")


    # ======================================================
    # Delete Student
    # ======================================================
    def delete_student(self):

        print("\n----- Delete Student -----")

        name = input("Enter Student Name : ")

        for student in self.students:

            if student["name"].lower() == name.lower():

                self.students.remove(student)

                print("\n Student Deleted Successfully")

                return

        print("\n Student Not Found")


# ==========================================================
# Main Program
# ==========================================================

manager = StudentManager()


while True:

    print("\n================================")
    print(" STUDENT RECORD MANAGEMENT SYSTEM ")
    print("================================")

    print("1. Add Student")
    print("2. Show Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("\nEnter Your Choice : ")


    if choice == "1":

        manager.add_student()

    elif choice == "2":

        manager.show_students()

    elif choice == "3":

        manager.search_student()

    elif choice == "4":

        manager.update_student()

    elif choice == "5":

        manager.delete_student()

    elif choice == "6":

        print("\nThank You For Using Student Record System")
        break

    else:

        print("\n Invalid Choice")