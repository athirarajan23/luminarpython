employees=[{"eid":1000,"name":"ajay","salary":25000,"designation":"developer"},
{"eid":1001,"name":"vijay","salary":22000,"designation":"developer"},
{"eid":1002,"name":"arun","salary":26000,"designation":"qa"},
{"eid":1003,"name":"varun","salary":27000,"designation":"ba"},
{"eid":1004,"name":"ram","salary":20000,"designation":"mrkt"}]

# aname=list(map(lambda name:name["name"],employees))
# print(aname)
# empname=list(map(lambda name:name["name"].upper(),employees))
# print(empname)
# name=list(filter(lambda emp:emp["name"][0]=='a',employees))
# print(name)
# sal=list(filter(lambda emp:emp["salary"]>23000,employees))
# print(sal)
# des=list(filter(lambda emp:emp["designation"]=='developer' and emp["salary"]>24000,employees))
# print(des)

#using reduce print highest sal
from functools import reduce
high_sal=reduce(lambda sal1,sal2:sal1 if sal1>sal2 else sal2,
                list(map(lambda emp:emp["salary"],employees)))
print(high_sal)




#using list comprehension solving questions
e_names=[emp["name"] for emp in employees]   #only names
print(e_names)
e_names=[emp["name"].upper() for emp in employees]   #all names in capitals
print(e_names)
e_names=[emp["name"] for emp in employees if emp["name"][0]=='a']   #starting with a names
print("names",e_names)
salary=[emp for emp in employees if emp["salary"]>23000]
print(salary)