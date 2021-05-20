try:
    a = int(input("enter a value"))
    b = int(input("enter a value"))
    print(a+b)
except:
    print("plz enter a integer value ")
finally:
    print("inside finally")
 #here try and catch works both at a time