age=int(input("enter your age"))
sex=input("enter ur sex as male or female")
ms=input("enter ur ms")
print("place of service")
if(sex=='female'):
    print(sex,"work only in urb areas")
elif(sex=='male') and (20<=age<=40):
    print("work anywhere")
elif(40<=age<60):
    print("work in urb only")
else:
    print("error")