class Subtraction:
    def sub(self,n1,n2):
        self.n1=n1
        self.n2=n2
    def printvalue(self):
        print(self.n1 - self.n2)
obj=Subtraction()
obj.sub(1, 1)
obj.printvalue()