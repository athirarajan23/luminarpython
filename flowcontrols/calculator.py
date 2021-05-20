opr=input("enter the operation ")
def add():
    num1=int(input("enter a number"))
    num2=int(input("enter a number"))
    print(num1+num2)
def sub():
    num1 = int(input("enter a number"))
    num2 = int(input("enter a number"))
    print(num1-num2)
def mul():
    num1 = int(input("enter a number"))
    num2 = int(input("enter a number"))
    print(num1*num2)
def div():
    num1 = int(input("enter a number"))
    num2 = int(input("enter a number"))
    print(num1/num2)
if(opr=="+"):
    add()
elif(opr=="-"):
    sub()
elif(opr=="*"):
    mul()
elif(opr=="/"):
    div()
else:
    print("invalid")


