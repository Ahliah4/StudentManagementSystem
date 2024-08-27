class Student:
    def __init__(self, student_id, name, age, major):
        # Initialize the Student object with ID, name, age, and major
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major

    def update_name(self, name):
        # Update the student's name
        self.name = name

    def update_age(self, age):
        # Update the student's age
        self.age = age

    def update_major(self, major):
        # Update the student's major
        self.major = major

    def display(self):
        # Display the student's details
        print(f"ID: {self.student_id}, Name: {self.name}, Age: {self.age}, Major: {self.major}")


class StudentDatabase:
    def __init__(self):
        # Initialize the StudentDatabase with an empty dictionary to store students
        self.students = {}

    def add_student(self, student):
        # Add a student to the database using their student ID as the key
        self.students[student.student_id] = student

    def remove_student(self, student_id):
        # Remove a student from the database if their ID exists
        if student_id in self.students:
            del self.students[student_id]

    def get_student(self, student_id):
        # Retrieve a student from the database by their ID
        return self.students.get(student_id, None)

    def display_all_students(self):
        # Display all students in the database
        if not self.students:
            print("No students in the database.")
        else:
            for student in self.students.values():
                student.display()


class StudentManagementSystem:
    def __init__(self):
        # Initialize the system with an empty StudentDatabase
        self.database = StudentDatabase()

    def add_new_student(self, student_id, name, age, major):
        # Add a new student to the system after checking for ID duplication
        if self.database.get_student(student_id):
            print("Student with this ID already exists.")
        else:
            student = Student(student_id, name, age, major)
            self.database.add_student(student)
            print("Student added successfully.")

    def delete_student(self, student_id):
        # Delete a student from the system by their ID
        if self.database.get_student(student_id):
            self.database.remove_student(student_id)
            print("Student deleted successfully.")
        else:
            print("Student not found.")

    def update_student_info(self, student_id, name=None, age=None, major=None):
        # Update the details of an existing student
        student = self.database.get_student(student_id)
        if student:
            if name:
                student.update_name(name)
            if age:
                student.update_age(age)
            if major:
                student.update_major(major)
            print("Student information updated successfully.")
        else:
            print("Student not found.")

    def show_all_students(self):
        # Display all students in the system
        self.database.display_all_students()

    def run_menu(self):
        # Run the text-based menu for interacting with the system
        while True:
            print("\nStudent Management System")
            print("1. Add Student")
            print("2. Delete Student")
            print("3. Update Student Information")
            print("4. View All Students")
            print("5. Exit")
            choice = input("Select an option: ")

            if choice == '1':
                # Add a new student
                student_id = input("Enter student ID: ")
                name = input("Enter student name: ")
                age = int(input("Enter student age: "))
                major = input("Enter student major: ")
                self.add_new_student(student_id, name, age, major)

            elif choice == '2':
                # Delete a student
                student_id = input("Enter student ID to delete: ")
                self.delete_student(student_id)

            elif choice == '3':
                # Update student information
                student_id = input("Enter student ID to update: ")
                name = input("Enter new name (press Enter to skip): ")
                age = input("Enter new age (press Enter to skip): ")
                major = input("Enter new major (press Enter to skip): ")

                # Convert age to an integer if provided
                age = int(age) if age else None
                self.update_student_info(student_id, name=name, age=age, major=major)

            elif choice == '4':
                # View all students
                self.show_all_students()

            elif choice == '5':
                # Exit the system
                print("Exiting the system.")
                break

            else:
                # Handle invalid menu choices
                print("Invalid choice. Please select a valid option.")


# Example usage with the menu system
if __name__ == "__main__":
    system = StudentManagementSystem()
    system.run_menu()
