class Person:
    def details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        print(self.name)
        print(self.age)
        print(self.gender)


class Sub:
    def sprint(self, mob, address):
        self.mob = mob
        self.address = address
        print(self.mob)
        print(self.address)


class Child(Person, Sub):
    def print(self, empid, post):
        self.empid = empid
        self.post = post
        print(self.empid)
        print(self.post)


class Parent(Person):
    def info(self, salary, experience):
        self.salary = salary
        self.experience = experience
        print(self.salary)
        print(self.experience)


class Student(Parent):
    def det(self, std, sub):
        self.std = std
        self.sub = sub
        print(self.std)
        print(self.sub)
per = Person()
per.details("Athi", 24, "Female")
s = Sub()
s.sprint("1234567890", "calicut")
ch = Child()
ch.details("vishnu", 26, "Male")
ch.sprint("451278963", "meenchandha")
ch.print(1, "SM")
p = Parent()
p.details("mini", 35, "female")
p.info(50000, 4)
st = Student()
st.details("Kichu", 23, "male")
st.info(75000, 6)
st.det(5, "django")