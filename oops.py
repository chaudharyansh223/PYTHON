class BankAccount:
    def __init__(self, acc_holder, initia_balance = 0):
        self.account_holder = acc_holder
        self.initial_balance = initia_balance
        self.transaction = []


    def add_amount(self,amt):
        if not amt < 0:
            print(f"current balance {self.initial_balance}")
            self.initial_balance+=amt
            self.transaction.append((self.account_holder, amt))
            print(f"Amount deposit {amt} by {self.account_holder}")

    def withdrawal(self,amt):
        if amt < 0:
            print("not enough balance to withdraw")
            return
        if amt > self.initial_balance:
            print("transaction can't be placed")
            return
        else:
            self.initial_balance-=amt
            self.transaction.append((self.account_holder, amt))
            return
    def get_transaction(self):
        print(f"current balance is {self.initial_balance}")
        print(f"total transaction are: {self.transaction}\n")

user1 = BankAccount("rahul")
user1.add_amount(2000)
user1.withdrawal(500)
user1.get_transaction()

user2 = BankAccount("sumit")
user2.add_amount(500)
user2.withdrawal(500)
user2.get_transaction()

user3 = BankAccount("ansh")
user3.add_amount(-100)
user3.withdrawal(-500)
user3.get_transaction()




