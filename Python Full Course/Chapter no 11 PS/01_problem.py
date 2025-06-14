# Problem no 01:


# Create a class (2-D vector) and use it to create another class representing a 3-D  vector.


class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"The 2D vector is {self.x}i +  {self.y}j .")


class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def show(self):
        print(f"The 3D vector is {self.x}i + {self.y}j + {self.z}k.")


a = Vector2D(9,3)
a.show()
b = Vector3D(6,3,7)
b.show()


print("This program was developed by Engr. Muhammad Javed.")
