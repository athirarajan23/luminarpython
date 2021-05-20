class Employee:
    def details(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.name)
        print(self.dept)
        print(self.salary)
obj=Employee()
obj.details("athira","HR",45000)
obj.printvalue()