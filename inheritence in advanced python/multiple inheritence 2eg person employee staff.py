class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Employee:
    def print(self):
        print("i work in luminar")
class Staff(Person,Employee):
    def info(self,salary,designation):
        self.salary=salary
        self.designation=designation
        print(self.salary)
        print(self.designation)
per=Person()
per.details("anjana",21)
emp=Employee()
emp.print()
st=Staff()
st.details("vishnu",26)
st.print()
st.info(60000,"CEO")