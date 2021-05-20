class Book:
    def properties(self,name):
        self.name=name
        print(self.name)
    def ages(self,age):
        self.age=age
        print(self.age)
class Author(Book):
    def ages(self,age):
        self.age=age
        print(self.age)
auth=Author()
auth.ages(22)