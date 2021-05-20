for i in range(1,4): #i,2,3     1,2,3
    for j in range(1,4):  #1,2,3    1 2 3 1 2 3 1 2 3
        print(i)   #1 1 1 2 2 2 3 3 3



for i in range(1,4): #4
    for j in range(1,4): #4 5 6 7 4 5 6 7
        print(j,end=" ") #4 5 6
    print()


for i in range(1,4):     #i=1
    for j in range(1,i+1):   #1,i+1=2
        print(j,end=" ")
    print()