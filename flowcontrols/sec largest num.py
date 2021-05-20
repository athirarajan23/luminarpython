num1=int(input("enter a number"))
num2=int(input("enter a number"))
num3=int(input("enter a number"))
if(num1>num2) and (num1>num3):
    if(num2>num3):
     print(num2,"the second largest number ")
    else:
     print(num3, "the second largest number")
elif(num2>num1) and (num2>num3):
    if(num1 > num3):
        print(num1, "the second largest number ")
    else:
        print(num3, "the second largest number")
elif(num3>num2)&(num3>num1):
    if(num1>num2):
        print(num1, "the second largest number ")
    else:
        print(num2, "the second largest number")
