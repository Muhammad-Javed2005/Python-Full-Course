# Problem no 07:

# Override the _len_() method on vector of problem 5 to display the dimension of the 
# vector.


class Vector:
    def __init__(self, l): 
        self.l = l

    
    
    def __len__(self):
        return len(self.l)

# Test the implementation
v1 = Vector([1, 2, 3]) 
print(len(v1))


print("This program was developed by Engr. Muhammad Javed.")
