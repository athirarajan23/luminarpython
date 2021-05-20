class Student:
    school="SDIT"
    def __init__(self,name,rollno,std):
        self.name=name
        self.rollno=rollno
        self.std=std

    def printval(self):
        print("name", self.name)
        print("rollno", self.rollno)
    def __str__(self):
        return self.name+str(self.rollno)
st = Student("athira",2,5)
st.printval()
print(st)
