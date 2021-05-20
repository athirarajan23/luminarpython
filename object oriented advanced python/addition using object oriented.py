class Addition:
    def add(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def printval(self):
        print(self.num1+self.num2)
obj=Addition()
obj.add(1,1)
obj.printval()