class UPI:
    def pay(self):
        print("Payment made using UPI")


class Paytm:
    def pay(self):
        print("Payment made using Paytm")


class GooglePay:
    def pay(self):
        print("Payment made using Google Pay")


class PaymentProcessor:
    def __init__(self, strategy):
        self.strategy = strategy

    def process(self):
        self.strategy.pay()


p = PaymentProcessor(UPI())
p.process()

p = PaymentProcessor(Paytm())
p.process()

p = PaymentProcessor(GooglePay())
p.process()