class Calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        print(self.num1)
        print(self.num2)
        print("sum=",self.num1+self.num2)
    def sub(self):
        print(self.num1)
        print(self.num2)
        print("difference=", self.num1 - self.num2)
    def div(self):
        print(self.num1)
        print(self.num2)
        print("result=", self.num1 / self.num2)
    def mul(self):
        print(self.num1)
        print(self.num2)
        print("product=", self.num1 * self.num2)
c=Calculator(4,2)
c.add()
c.sub()
c.div()
c.mul()

