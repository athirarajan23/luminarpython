class Person:
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Employee(Person):
    def print(self,company,salary):
        self.company=company
        self.salary=salary
        print(self.company)
        print(self.salary)
per=Person()
per.setval("radhika",20,"female")
emp=Employee()
emp.setval("athi",25,"female")
emp.print("luminar",50000)