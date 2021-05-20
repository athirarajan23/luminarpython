#read a limit and print prime numbers under that limit

ll=int(input("enter a limit"))
ul=int(input("enter a limit"))
sum=0
for n in range(ll,ul+1):
    if(n>1):
        for i in range(2,n):
            if(n%i==0):
                break
        else:
            print(n)
            sum+=n
print(sum)