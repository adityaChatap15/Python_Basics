class Account:
    def __init__(self, accNo, bal):
        self.accountNo = accNo
        self.balance = bal

    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "debited from your account !")
        print("Total Balance remaining is ", self.total_bal())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "credited to your account !")
        print("Total Balance is", self.total_bal())

    def total_bal(self):
        return self.balance

acc1 = Account("234CB55466", 30000)
acc1.credit(5000)
acc1.debit(2000)
acc1.total_bal()