# str="mad"
# a=" "
# for i in str:
#     a=i+a
# if(str==a):
#     print("palindrome")
# else:
#     print("not a palindrome")
# print(a)



str=input("enter a value")
pal=str[::-1]
if str==pal:
    print("palindrome")
else:
    print("not a palindrome")

