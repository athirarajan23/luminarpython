class Vehicle:
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def printval(self):
        print("name",self.name)
        print("color",self.color)
class Bus(Vehicle):
    def __init__(self,brand,cost,name,color):
        super().__init__(name,color)
        self.brand=brand
        self.cost=cost
    def print(self):
        print(self.brand)
        print(self.cost)
b=Bus("maruthi",200000,"wagnor","white")
b.printval()
b.print()