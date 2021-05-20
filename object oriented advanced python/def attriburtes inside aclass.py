class Person:
    def details(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
obj=Person()
obj.details("athira",23)
obj.printval()