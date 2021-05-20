class Student:
        def __init__(self,name,rollno,department,marks):
            self.name=name
            self.rollno=rollno
            self.department=department
            self.marks=marks
        def printval(self):
            print("name",self.name)
            print("rollno",self.rollno)
            print("department",self.department)
            print("marks",self.marks)
        def __str__(self):
            return self.name
f=open("work1.txt","r")
for line in f:
    data = line.rstrip("\n").split(",")
    if(int(data[3])>190):
        name= data[0]
        rollno = data[1]
        department= data[2]
        marks= data[3]
        s = Student(name,rollno,department,marks)
        print(s)
        s.printval()