class Handler:
    def __init__(self):
        self.next_handler = None

    def set_next(self, handler):
        self.next_handler = handler

    def handle(self, req):
        if self.next_handler:
            self.next_handler.handle(req)
        else:
            print("All handlers failed")
            return None

class CashHandler(Handler):
    def handle(self, req):
        if req['method'] == "cash":
            print(f"Processing cash {req['amount']} won")
            return
        else:
            print("CashHandler cannot process")
            super().handle(req)

class CreditCardHandler(Handler):
    def handle(self, req):
        if req['method'] == "creditCard":
            print(f"Processing credit card {req['amount']} won")
            return
        else:
            print("CreditCardHandler cannot process")
            super().handle(req)

class DebitCardHandler(Handler):
    def handle(self, req):
        if req['method'] == "debitCard":
            print(f"Processing debit card {req['amount']} won")
            return
        else:
            print("DebitCardHandler cannot process")
            super().handle(req)

class PaypalHandler(Handler):
    def handle(self, req):
        if req['method'] == "paypal":
            print(f"Processing PayPal {req['amount']} won")
            return
        else:
            print("PaypalHandler cannot process")
            super().handle(req)

class BitcoinHandler(Handler):
    def handle(self, req):
        if req['method'] == "bitcoin":
            print(f"Processing bitcoin {req['amount']} won")
            return
        else:
            print("BitcoinHandler cannot process")
            super().handle(req)

cash_handler = CashHandler()
creditcard_handler = CreditCardHandler()
debitcard_handler = DebitCardHandler()
paypal_handler = PaypalHandler()
bitcoin_handler = BitcoinHandler()

cash_handler.set_next(creditcard_handler)
creditcard_handler.set_next(debitcard_handler)
debitcard_handler.set_next(paypal_handler)
paypal_handler.set_next(bitcoin_handler)

payment = {"method": "debitCard", "amount": 10000}

cash_handler.handle(payment)
