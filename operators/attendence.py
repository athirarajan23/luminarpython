number=int(input("enter the number of class held"))
attentedclass=int(input("enter the number of class attended"))
percentage=(attentedclass/number)*100
if(percentage>=75):
    print(percentage,"attendence so allowed")
else:
    print(percentage,"not allowed")


