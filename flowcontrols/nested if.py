#current year-bornyear
#date also have to be print

year=int(input("enter current year"))
month=int(input("enter current month"))
date=int(input("enter current day"))
dobyear=int(input("enter  year"))
dobmonth=int(input("enter month"))
dobdate=int(input("enter day"))
yeardiff=year-dobyear
monthdiff=month-dobmonth
datediff=date-dobdate
if(dobyear==year)&(dobmonth==month):   #1997<2021
    age=year-dobyear
    print("he/she is",age,"years old")
else:
    year-=1
    age=year-dobyear
    print(age)



