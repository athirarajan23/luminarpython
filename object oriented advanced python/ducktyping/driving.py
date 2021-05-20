class Swift:
    def accelarate(self):
        print("swift accelaritng ")
    def breaking(self):
        print("break using swift car")
class Vagnor:
    def accelarate(self):
        print("Vagnor accelaritng ")
    def breaking(self):
        print("break using vagnor car")
class Person:
    def driving(self,func):
        func.accelarate()
        func.breaking()
v=Vagnor()
p=Person()
p.driving(v)