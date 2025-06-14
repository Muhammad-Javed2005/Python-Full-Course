def safe_divide():
    try:
        num1 = int(input("Enter numerator: "))
        num2 = int(input("Enter denominator: "))
        result = num1 / num2
    except ValueError:
        print(" Please enter valid integers only.")
    except ZeroDivisionError:
        print(" Division by zero is not allowed.")
    else:
        print(f" Division successful. Result: {result}")
    finally:
        print("Operation completed.")

safe_divide()



print("This program was developed by Engr. Muhammad Javed.")


