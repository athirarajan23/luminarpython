# constructor: to initialise instance variables
# constructor automatically invoke when creating object

class Person:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def printval(self):
        print(self.name)
        print(self.age)
        print(self.gender)
obj=Person("athira",23,"female")
obj.printval()