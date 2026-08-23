class netBanking:

    def payment(self, amount):
        print("Payment Amount = ", amount)
        print("Payment made using Net Banking")

class UPI:
    def payment(self, amount):
        print("Payment Amount = ", amount)
        print("Payment made using UPI")

class credit:
    def payment(self, amount):
        print("Payment Amount = ", amount)
        print("Payment made using Credit Card")

class debit:
    def payment(self, amount):
        print("Payment Amount = ", amount)
        print("Payment made using Debit Card")

class Transaction:

    def __init__(self, mode):

        self.mode = mode

    def pay(self, amount):

        self.mode.payment(amount)

amount = int(input("Enter the payment amount : "))
choice = int(input("Enter the payment method : \n1. Net Banking\n2. UPI\n3. Credit Card\n4. Debit Card\n> "))


if choice == 1:
    payment = Transaction(netBanking())

elif choice == 2:
    payment = Transaction(UPI())

elif choice == 3:
    payment = Transaction(credit())

elif choice == 4:
    payment = Transaction(debit())

payment.pay(amount)
