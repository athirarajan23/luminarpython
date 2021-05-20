#lower to upper even numbers
ll=int(input("enter the limit"))
ul=int(input("enter the limit"))
for i in range(ll,ul+2):
    if(i%2==0):
        print(i)
