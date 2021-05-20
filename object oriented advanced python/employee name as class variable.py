class Employee:
    company_name="LUMINAR"
    def details(self,name,dept,salary):
        self.name=name
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print(self.name)
        print(self.dept)
        print(self.salary)
        print(Employee.company_name)
obj=Employee()
obj.details("athira","HR",45000)
obj.printvalue()
obj.details("BIJOY","TEA SUPPLIER",5)
obj.printvalue()