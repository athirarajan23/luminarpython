low=int(input("enter the limit"))      #1
upp=int(input("enter the limit"))      #10
sumeven=0
sumodd=0
for i in range(low,upp+1):   #1 to 10 checked
    if(i%2==0):             #
        sumeven+=i
    else:
        sumodd+=i
print(sumeven)
print(sumodd)

