try:
    a = int(input(" Please enter a number: "))
    print(f" You entered: {a}")

except ValueError as ve:
    print(" Invalid input! You must enter a valid number.")
    print(f"Error details: {ve}")

except Exception as ex:
    print(" Oops! Something unexpected went wrong.")
    print(f"Error details: {ex}")

print(" Thank you for using the program!")


print("This program was developed by Engr. Muhammad Javed.")

