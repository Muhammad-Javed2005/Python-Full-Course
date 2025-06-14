# File: 4_inheritance.py
"""
Inheritance Example: Real-world Complex Example - University System
"""

# Inheritance ka matlab ek class dusri class ke properties aur methods inherit karti hai
# Yeh example ek university system ka hai jisme multiple roles aur functionalities hain

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}"

# Student class inherit karti hai Person se
class Student(Person):
    def __init__(self, name, age, student_id, courses=None):
        super().__init__(name, age)
        self.student_id = student_id
        self.courses = courses if courses else []

    def enroll_course(self, course):
        self.courses.append(course)

    def get_details(self):
        base = super().get_details()
        return f"{base}, Student ID: {self.student_id}, Courses: {', '.join(self.courses)}"

# Teacher class bhi inherit karti hai Person se
class Teacher(Person):
    def __init__(self, name, age, employee_id, subjects=None):
        super().__init__(name, age)
        self.employee_id = employee_id
        self.subjects = subjects if subjects else []

    def assign_subject(self, subject):
        self.subjects.append(subject)

    def get_details(self):
        base = super().get_details()
        return f"{base}, Employee ID: {self.employee_id}, Subjects: {', '.join(self.subjects)}"

# Admin class inherit karti hai Teacher se (kyunki admin bhi teacher ho sakta hai)
class Admin(Teacher):
    def __init__(self, name, age, employee_id, role):
        super().__init__(name, age, employee_id)
        self.role = role

    def get_details(self):
        base = super().get_details()
        return f"{base}, Role: {self.role}"

# Examples bana rahe hain
student1 = Student("Javed", 20, "S123")
student1.enroll_course("Python")
student1.enroll_course("Math")
print("\nStudent Details:")
print(student1.get_details())

teacher1 = Teacher("Jiya", 35, "T987")
teacher1.assign_subject("Data Science")
teacher1.assign_subject("AI")
print("\nTeacher Details:")
print(teacher1.get_details())

admin1 = Admin("Ghulam", 45, "T001", "Dean")
admin1.assign_subject("Management")
print("\nAdmin Details:")
print(admin1.get_details())


print("This program was developed by Engr. Muhammad Javed.")
