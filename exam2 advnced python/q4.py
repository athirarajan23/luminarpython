class Animal:
    def _init_(self,name,age):
        self.name=name
        self.age=age
        print("Name:",self.name)
        print("Age:",self.age)
class Dog():
    def dogmod(self,mod,color):
        self.mod=mod
        self.color=color
        print("Mode:",self.mod)
        print("Color:",self.color)
class Pom(Dog):
    def features(self,name,age,color):
        self.name=name
        self.age=age
        self.color=color
        print(self.name)
        print(self.age)
        print(self.color)
d=Dog()
d.dogmod("Pug","Brown")
p=Pom()
p.dogmod("Pom","Black")
p.features("Julie",1,"white")