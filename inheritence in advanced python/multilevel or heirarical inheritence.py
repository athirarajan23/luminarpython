class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Employee(Person):
    def print(self,emp_company):
        self.emp_company=emp_company
        print(self.emp_company)
class Staff(Employee):
    def info(self,salary):
        self.salary=salary
        print(self.salary)
per=Person()
per.details("SITHA",26)
emp=Employee()
emp.details("arun",28)
emp.print("abc")
st=Staff()
st.details("akshay",24)
st.print("luminar")
st.info(30000)