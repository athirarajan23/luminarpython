class Employee:
    company_name="LUMINAR"
    def __init__(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.name)
        print(self.dept)
        print(self.salary)
        print(Employee.company_name)
    def __str__(self):
        return str(self.dept)
obj=Employee("athira","HR",45000)
obj.printvalue()
print(obj)