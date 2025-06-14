"""
Encapsulation Example: Hiding Data
"""

# Encapsulation ka matlab hota hai data ko hide karna direct access se
# Hum __ (double underscore) use karte hain private banane ke liye

class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount  # Private access allowed within class

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount("Javed", 5000)
acc.deposit(1500)
acc.withdraw(2000)
print("Balance:", acc.get_balance())  # Accessing through public method


print("This program was developed by Engr. Muhammad Javed.")
