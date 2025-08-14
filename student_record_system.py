import json
import os

DATA_FILE = "students.json"

# Load data from file
def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as file:
        return json.load(file)

# Save data to file
def save_data(data):
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Add student
def add_student(data):
    roll = input("Enter Roll Number: ")
    for student in data:
        if student["roll"] == roll:
            print("Student with this roll number already exists!")
            return
    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    student = {
        "roll": roll,
        "name": name,
        "age": age,
        "course": course
    }
    data.append(student)
    print("Student added successfully.")

# View all students
def view_students(data):
    if not data:
        print("No student records found.")
        return
    print("\n--- Student Records ---")
    for student in data:
        print(f"Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
    print("------------------------")

# Search student
def search_student(data):
    roll = input("Enter Roll Number to search: ")
    for student in data:
        if student["roll"] == roll:
            print(f"Found: Roll: {student['roll']}, Name: {student['name']}, Age: {student['age']}, Course: {student['course']}")
            return
    print("Student not found.")

# Update student
def update_student(data):
    roll = input("Enter Roll Number to update: ")
    for student in data:
        if student["roll"] == roll:
            print(f"Current Name: {student['name']}")
            student["name"] = input("Enter new name: ") or student["name"]
            student["age"] = input("Enter new age: ") or student["age"]
            student["course"] = input("Enter new course: ") or student["course"]
            print("Student updated successfully.")
            return
    print("Student not found.")

# Delete student
def delete_student(data):
    roll = input("Enter Roll Number to delete: ")
    for i, student in enumerate(data):
        if student["roll"] == roll:
            del data[i]
            print("Student deleted successfully.")
            return
    print("Student not found.")

# Menu
def main():
    data = load_data()
    while True:
        print("\n--- Student Record System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")
        choice = input("Choose an option (1-6): ")

        if choice == "1":
            add_student(data)
        elif choice == "2":
            view_students(data)
        elif choice == "3":
            search_student(data)
        elif choice == "4":
            update_student(data)
        elif choice == "5":
            delete_student(data)
        elif choice == "6":
            save_data(data)
            print("Data saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
