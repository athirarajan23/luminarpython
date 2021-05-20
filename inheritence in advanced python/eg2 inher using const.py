class Employee:
    def __init__(self,name,company):
        self.name=name
        self.company=company
    def printval(self):
        print("name",self.name)
        print("company",self.company)
class Staff(Employee):
    def __init__(self,stfnum,salary,name,company):
        super().__init__(name,company)
        self.stfnum=stfnum
        self.salary=salary
    def print(self):
        print(self.stfnum)
        print(self.salary)
cr=Staff(3,35000,"ATHI","LUMINAR")
cr.printval()
cr.print()