# a=int(input("enter a number"))
# b=int(input("enter a number"))
# print(a/b)

#to solve unexpected errors exception handle is used

a=int(input("enter a number"))
b=int(input("enter a number"))
try:
    print(a/b)
except:
    print("exception occured")

#try and exception wont work at once but at some cases it works at a time.