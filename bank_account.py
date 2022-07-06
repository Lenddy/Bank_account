class Bank_account:
    def __init__(self,balance = 0,int_rate=0.01):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        current_balance = self.balance
        new_balance = current_balance + amount
        self.balance = new_balance


    def withdraw(self,amount):
        curent_balance = self.balance
        new_balance=curent_balance - amount
        self.balance = new_balance



    def display_account_info(self):
        print("Your balance is",self.balance)
        print("your interest rate is ", self.int_rate)


    def yield_int_rate(self):
        if self.balance > 0:
            self.balance += self.int_rate* self.balance

l = Bank_account(100)
l.display_account_info()

print("")

l.deposit(100)
l.display_account_info()

print("")

l.yield_int_rate()
l.display_account_info()

print("")

l.withdraw(50)
l.display_account_info()




class Bank_account:
    def __init__(self,balance = 0,int_rate=0.01):
        self.int_rate = int_rate
        self.balance = balance


    def deposit(self,amount):
        current_balance = self.balance
        new_balance = current_balance + amount
        self.balance = new_balance
        return self


    def withdraw(self,amount):
        curent_balance = self.balance
        new_balance=curent_balance - amount
        self.balance = new_balance
        return self


    def display_account_info(self):
        print("Your balance is",self.balance)
        print("your interest rate is ", self.int_rate)
        return self


    def yield_int_rate(self):
        if self.balance > 0:
            self.balance += self.int_rate* self.balance
        return self


r = Bank_account()
r.deposit(500).deposit(500).withdraw(100).withdraw(100).withdraw(100).withdraw(100).yield_int_rate().display_account_info()