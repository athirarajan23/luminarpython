sub1=int(input("enter a number"))
sub2=int(input("enter a number"))
sub3=int(input("enter a number"))
sub4=int(input("enter a number"))
total=(sub1+sub2+sub3+sub4)
print(total)
if(total>=180)&(total<=200):
    print("grade is A+")
elif(total>=160)&(total<=179):
    print("grade is A")
elif(total>=140)&(total<=159):
    print("grade is B+")
elif(total>=120)&(total<=139):
    print("grade is B")
elif(total>=100)&(total<=119):
    print("grade is c+ ")
elif(total>=80)&(total<=99):
    print("grade c")
elif(total>=60)&(total<=79):
    print("grade D+")
else:
    print("fail")
