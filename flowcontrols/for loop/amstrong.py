#amstrong number is a number when takes cube returns that number eg 1^3+5^3+3^3=153

a=int(input("enter a number"))
sum=0
temp=a
while temp>0:
    dig=temp%10
    sum+=dig**3
    temp//=10
if a==sum:
    print("amstrong")
else:
    print("not amstrong")