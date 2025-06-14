# Read lines function:

f = open("myfile.txt","r")
print(f.readlines())
f.close()

f = open("myfile.txt","r")

line1 = f.readline()
print(line1,type(line1))

line2= f.readline()
print(line2,type(line2))

line3 = f.readline()
print(line3,type(line3))

line4 = f.readline()
print(line4,type(line4))

line5 = f.readline()
print(line5,type(line5))

line6 = f.readline()
print(line6,type(line6))

f.close()

f = open("myfile.txt")
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()


print("This program was developed by Engr. Muhammad Javed.")

