class Studentt:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print(self.name)
        print(self.age)
    def __str__(self):
        return self.name
f=open("student", "r")
for i in f:
    data=i.rstrip("\n").split(",")   #split is used to split data using comma  #to strip something we use strip in this prgm \n is striped
    #print(data)
    name=data[0]
    age=data[1]
    obj=Studentt(name,age)
    print(obj)
    obj.printval()