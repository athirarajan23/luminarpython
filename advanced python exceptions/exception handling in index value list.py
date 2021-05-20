list=[1,2,3]
a=int(input("enter"))
try:
    print(list[a])
except:
    print("exception handling")
finally:
    print("inside finally") #work when either try or except is working