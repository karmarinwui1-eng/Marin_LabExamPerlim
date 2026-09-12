class Student:
    def __init__(self, student_id, student_name, course, year_level):
        self.student_id = student_id
        self.student_name = student_name
        self.course = course
        self.year_level = year_level


class DynamicArray:
    def __init__(self):
        self.capacity = 5
        self.size = 0
        self.students = [None] * self.capacity

    def append(self, student):
        if self.size == self.capacity:
            self._resize()

        self.students[self.size] = student
        self.size += 1

    def _resize(self):
        self.capacity *= 2
        new_students = [None] * self.capacity

        for i in range(self.size):
            new_students[i] = self.students[i]

        self.students = new_students

    def get(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        return self.students[index]

    def set(self, index, student):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        self.students[index] = student

    def display(self):
        if self.size == 0:
            print("No students found.")

        for i in range(self.size):
            student = self.get(i)

            print(f"Student ID: {student.student_id}")
            print(f"Student Name: {student.student_name}")
            print(f"Course: {student.course}")
            print(f"Year Level: {student.year_level}")
            print()

    def search(self, student_id):
        for i in range(self.size):
            student = self.get(i)

            if student.student_id == student_id:
                print(f"Student ID: {student.student_id}")
                print(f"Student Name: {student.student_name}")
                print(f"Course: {student.course}")
                print(f"Year Level: {student.year_level}")
                return

        print("Student not found.")

    def update(self, student_id, new_name, new_course, new_year_level):
        for i in range(self.size):
            student = self.get(i)

            if student.student_id == student_id:
                new_student = Student(
                    student_id,
                    new_name,
                    new_course,
                    new_year_level
                )

                self.set(i, new_student)
                return

        print("Student not found.")

    def remove(self, student_id):
        for i in range(self.size):
            student = self.get(i)

            if student.student_id == student_id:

                for j in range(i, self.size - 1):
                    self.students[j] = self.students[j + 1]

                self.students[self.size - 1] = None
                self.size -= 1
                return

        print("Student not found.")

    def display_array_info(self):
        print(f"Current number of students: {self.size}")
        print(f"Current array capacity: {self.capacity}")


records = DynamicArray()

while True:
    print("\n++++++++++++++++++++++++++++++++")
    print(" STUDENT RECORD MANAGER")
    print("--------------------------------")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Remove Student")
    print("6. Display Array Information")
    print("7. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        student_id = input("Enter Student ID: ")
        student_name = input("Enter Student Name: ")
        course = input("Enter Course: ")
        year_level = int(input("Enter Year Level: "))

        student = Student(
            student_id,
            student_name,
            course,
            year_level
        )

        records.append(student)

    elif choice == 2:
        records.display()

    elif choice == 3:
        student_id = input("Enter Student ID to search: ")
        records.search(student_id)
    elif choice == 4:
        student_id = input("Enter Student ID to update: ")
        new_name = input("Enter new Student Name: ")
        new_course = input("Enter new Course: ")
        new_year_level = int(input("Enter new Year Level: "))

        records.update(
            student_id,
            new_name,
            new_course,
            new_year_level
        )

    elif choice == 5:
        student_id = input("Enter Student ID to remove: ")
        records.remove(student_id)

    elif choice == 6:
        records.display_array_info()

    elif choice == 7:
        break

    else:
        print("Invalid choice.")