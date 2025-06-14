f = open("myfile.txt")
print(f.readlines)
f.close()


# The same can be written using with statement like this:


with open("myfile.txt") as f:
    print(f.readlines())

# The same can be written using with statement like this:

print("This program was developed by Engr. Muhammad Javed.")
