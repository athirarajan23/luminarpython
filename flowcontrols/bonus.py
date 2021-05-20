salary=int(input("enter your salary"))
expyear=int(input("enter your experience"))
if(expyear>5):
    print("salary(+bonus)=",salary+(salary)*5/100)
else:
    print("not eligible")