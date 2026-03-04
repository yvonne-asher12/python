#Yvonne Karimi
#BSCIT-05-0072/2024
class BankAccount:
    
    def __init__(self, acc_no, balance, dof_opening,cust_name):
        self.acc_no = acc_no
        self.balance = balance
        self.dof_opening = dof_opening
        self.cust_name = cust_name
    
    def deposit (self,amount):
        self.balance += amount
        return amount
    def withdrawal (self,amount):
        if amount > self.balance:
            return "Insufficient balance"
        else:
            self.balance -= amount
            return amount
    def check_balance(self):
        print("account balance:",self.balance)
    def cust_details(self):
        print("acc_no:",self.acc_no)
        print("balance:",self.balance)
        print("date::",self.dof_opening)
        print("customer_name:",self.cust_name)


acc = BankAccount("246" ,12000, "04-02-2026", "Asher")

print(acc.deposit(30000))
print(acc.withdrawal(10000))

acc.check_balance()
acc.cust_details()
    

