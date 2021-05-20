# person,child,parent,student
# parent-person,child inherit
# student-child inherit
#child-person inherit



class Person:
    def pdetais(self,name,age):
        self.name=name
        self.age=age
        print(self.name)
        print(self.age)
class Child(Person):
    def print(self):
        print("iam studing in phss")
class Parent(Person):
    def detais(self,pname,page):
        self.pname=pname
        self.page=page
        print(self.pname)
        print(self.page)
class Student(Child):
    def info(self,stname,stclass):
        self.stname=stname
        self.stclass=stclass
        print(self.stname)
        print(self.stclass)
per=Person()
per.pdetais("bibi",23)
ch=Child()
ch.pdetais("ardra",23)
ch.print()
p=Parent()
p.pdetais("diya",26)
p.detais("rajan",52)
st=Student()
st.print()
st.info("seetha",6)
st.pdetais("fara",28)