# Problem No 02:
# Write a program to fill in a letter template given below with name and date.



a = letter = '''Dear <|Name|>, 
                You are selected! 
                  <|Date|> '''
name = input("Enter your name :")
Date = input("Enter your interview date : ")
print(a.replace(f"<|Name|>,", name).replace("<|Date|>", Date))


print("This program was developed by Engr. Muhammad Javed.")
