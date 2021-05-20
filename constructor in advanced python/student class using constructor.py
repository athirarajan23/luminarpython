class Student:
    school="presentation higher secondary school"
    def __init__(self,name,roolno):
        self.name=name
        self.roolno=roolno
    def printval(self):
        print(self.name)
        print(self.roolno)
        print("school",Student.school)
obj=Student("athira",1)
obj.printval()
obj1=Student("vishnu",2)
obj1.printval()

