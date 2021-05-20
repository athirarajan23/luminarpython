# class Student:
#     def setval(self,name,id,college):
#         self.name=name
#         self.id=id
#         self.college=college
#     def printval(self):
#         print("name",self.name)
#         print("id",self.id)
#         print("college",self.college)
# st=Student()
# st.setval("athira",1,"abc")
# st.printval()


#since the college attribute is same for all students
#class variables ae related to class (student class ,college variable)
#instance variables are related to methods
class Student:
    college="luminar"
    def setval(self,name,id):
        self.name=name
        self.id=id
    def printval(self):
        print("name",self.name)
        print("id",self.id)
        print("college",Student.college)
st=Student()
st.setval("athira",1)
st.printval()