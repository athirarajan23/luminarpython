
#single inheritence

class Person:                        #base/super/parent class
    def setval(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
        print(self.name)
        print(self.age)
        print(self.gender)
class Student(Person):              #child/sub/derived class
    def print(self,department,college):
        self.department = department
        self.college = college
        print(self.department)
        print(self.college)
obj=Person()
obj.setval("athira",23,"female")
st=Student()
st.print("MCA","SDIT")
st.setval("ambi",25,"male")
