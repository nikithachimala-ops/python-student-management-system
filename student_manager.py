import csv
import os

FILE_NAME = "students.csv"


def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Name", "Age", "Course"])


def add_student():
    student_id = input("Enter Student ID: ")
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([student_id, name, age, course])

    print("✅ Student Added Successfully")


def view_students():
    print("\n--- Student List ---")
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)


def search_student():
    search_id = input("Enter Student ID: ")
    found = False

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == search_id:
                print("Student Found:", row)
                found = True

    if not found:
        print("❌ Student Not Found")


def update_student():
    update_id = input("Enter Student ID to Update: ")
    updated_data = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == update_id:
                print("Enter New Details")
                row[1] = input("New Name: ")
                row[2] = input("New Age: ")
                row[3] = input("New Course: ")
            updated_data.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(updated_data)

    print("✅ Student Updated")


def delete_student():
    delete_id = input("Enter Student ID to Delete: ")
    remaining_data = []

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] != delete_id:
                remaining_data.append(row)

    with open(FILE_NAME, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerows(remaining_data)

    print("✅ Student Deleted")