# 0 adding previous of 2 numbers is febinocci series
# 1
# 1
# 2
# 3
# 5
# 8
# 13

n=int(input("enter a limit"))
a=0
b=1
count=0
for i in range(0,n+1):
    print(a)
    count=a+b
    a=b
    b=count
    count+=1




