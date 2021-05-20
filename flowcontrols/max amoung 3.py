a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a number"))
if(a>b)&(a>c):
    print(a,"is the highest num")
elif(b>a)&(b>c):
    print(b, "is the highest num")
else:
    print(c,"is highest")