class Bank:
    bankname="canara"
    def account(self,name,accountnumber):
        self.name=name
        self.accountnumber=accountnumber
        self.minimumbalance = 1000
        self.balance=self.minimumbalance
        print(self.name)
        print(self.accountnumber)
        print(Bank.bankname)
        print(self.minimumbalance)
    def deposit(self,depositamount):
        self.depositamount=depositamount
        self.balance+=self.depositamount
        print(self.depositamount)
        print(self.balance)
    def withdraw(self,wdrlamt):
        self.wdrlamt=wdrlamt
        if self.wdrlamt>self.balance:
            print("insufficient balance")
        else:
            print("account debited with",self.wdrlamt)
            self.balance -= self.wdrlamt
            print("available balance=",self.balance)
obj=Bank()
obj.account("ravi",1)
obj.deposit(200)
obj.withdraw(50)


