range1=int(input("enter a range"))
range2=int(input("enter a range"))
for i in range(range1,range2+1):
    if (i%2==0): #1,num num=no of rows
    #print(i)
        r=6
        for k in range(r,0,-1):
            for j in range(0,k):
                print(i,end=" ")
            print("\r")
    else:
        r2=6
        for l in range(range2): #1,num num=no of rows
            for m in range(0,l+1):
                print(i,end=" ")
            print("\r")


