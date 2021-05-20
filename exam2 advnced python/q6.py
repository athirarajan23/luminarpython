class Student:
    def __init__(self,name,std,dept,mark):
        self.name=name
        self.std=std
        self.dept=dept
        self.mark=mark
        print(self.name)
        print(self.std)
        print(self.dept)
        print(self.mark)
lst=[]
f=open("store","r")
for i in f:
    data=i.rstrip("\n").split(",")
    name=data[0]
    std=data[1]
    dept=data[2]
    mark=data[3]
    s1=Student(name,std,dept,mark)
    lst.append(s1)
mark=[]
for st in lst:
    mark.append(st.mark)
print(mark)
for st in lst:
    if (st.mark==max(mark)):
        print(st.name,st.std,st.dept,st.mark)

