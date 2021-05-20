num=int(input("enter a number"))   #123
rev=0
while(num>0): #123>0
   n=num%10  #123%10 =3
   rev=rev*10+n   #0*10+3
   num=num//10  # 3//10
print(rev)
