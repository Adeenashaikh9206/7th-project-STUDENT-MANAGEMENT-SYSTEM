class StudentManagementSystem:
    # Constructor: Automatically creates an empty list for storing students
    def __init__(self):
        self.students = []

    # Method 1: Add a new student record
    def add_student(self):
        print("\n===== ADD STUDENT =====")
        student_id = input("Enter student ID: ").strip()
        name = input("Enter student name: ").strip().title()
        age = input("Enter student age: ").strip()
        course = input("Enter course name: ").strip().title()

        # Check empty information
        if student_id == "" or name == "" or age == "" or course == "":
            print("\n[ERROR] All information is required.")
            return

        # Check duplicate student ID
        for student in self.students:
            if student["id"] == student_id:
                print("\n[ERROR] This student ID already exists.")
                return

        # Create one student dictionary record
        student = {
            "id": student_id,
            "name": name,
            "age": age,
            "course": course
        }
        
        self.students.append(student)
        print("\n[SUCCESS] Student added successfully.")

    # Method 2: Update an existing student record
    def update_student(self):
        print("\n===== UPDATE STUDENT =====")
        if len(self.students) == 0:
            print("\n[INFO] No student records are available.")
            return

        student_id = input("Enter student ID to update: ").strip()

        for student in self.students:
            if student["id"] == student_id:
                print(f"\n[FOUND] Student found: {student['name']}")
                new_name = input("Enter new name: ").strip().title()
                new_age = input("Enter new age: ").strip()
                new_course = input("Enter new course: ").strip().title()

                if new_name == "" or new_age == "" or new_course == "":
                    print("\n[ERROR] New information cannot be empty.")
                    return

                student["name"] = new_name
                student["age"] = new_age
                student["course"] = new_course
                print("\n[SUCCESS] Student updated successfully.")
                return

        print("\n[ERROR] Student ID was not found.")

    # Method 3: Display all stored student records
    def view_students(self):
        print("\n===== ALL STUDENTS =====")
        if len(self.students) == 0:
            print("\n[INFO] No student records are available.")
            return

        for count, student in enumerate(self.students, 1):
            print(f"\n--- Record #{count} ---")
            print(f"Student ID : {student['id']}")
            print(f"Name       : {student['name']}")
            print(f"Age        : {student['age']}")
            print(f"Course     : {student['course']}")
        print("-" * 25)


# Execution Section
if __name__ == "__main__":
    # Create object
    system = StudentManagementSystem()

    # Interactive Menu Loop
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Add Student")
        print("2. Update Student")
        print("3. View All Students")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ").strip()
        
        if choice == "1":
            system.add_student()
        elif choice == "2":
            system.update_student()
        elif choice == "3":
            system.view_students()
        elif choice == "4":
            print("\nExiting Student Management System. Goodbye!")
            break
        else:
            print("\n[ERROR] Invalid choice. Please enter 1, 2, 3, or 4.")