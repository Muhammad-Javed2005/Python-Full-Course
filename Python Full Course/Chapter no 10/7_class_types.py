"""
Public, Private, Protected Variables
"""

class Student:
    def __init__(self):
        self.name = "Ali"               # public
        self._roll = 123                # protected
        self.__grade = "A"              # private

    def show(self):
        print("Name:", self.name)
        print("Roll:", self._roll)
        print("Grade:", self.__grade)

s = Student()
s.show()

# Accessing private variable using name mangling
print("Accessing private grade:", s._Student__grade)


print("This program was developed by Engr. Muhammad Javed.")

