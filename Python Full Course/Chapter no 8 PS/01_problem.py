# Problem no 01:
# Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):


    if(a>b and a>c):
        return a 
    elif(b>a and b>c):
        return b 
    else:
        return c 
    

a = int(input("Enter number 1 : "))
b = int(input("Enter number 2 : "))
c = int(input("Enter number 3 : ")) 
  
print(greatest(a,b,c))



print("This program was developed by Engr. Muhammad Javed.")
