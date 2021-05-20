class Employee:
    def package(self):
        print("10 lack per anum")
    def timerange(self):
        print("full time")

class ParttimeStaff(Employee):
    def timerange(self):
        print("parttime,5 lack per anum")
p=ParttimeStaff()
p.timerange()