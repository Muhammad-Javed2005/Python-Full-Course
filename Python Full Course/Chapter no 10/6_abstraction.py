"""
Abstraction Example: Payment System
"""
from abc import ABC, abstractmethod

class Payment(ABC):
    @abstractmethod
    def make_payment(self, amount):
        pass

class CreditCardPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid Rs.{amount} using Credit Card")

class PayPalPayment(Payment):
    def make_payment(self, amount):
        print(f"Paid Rs.{amount} using PayPal")

# Calling the abstracted interface

payment1 = CreditCardPayment()
payment2 = PayPalPayment()
payment1.make_payment(1500)
payment2.make_payment(2200)


print("This program was developed by Engr. Muhammad Javed.")
