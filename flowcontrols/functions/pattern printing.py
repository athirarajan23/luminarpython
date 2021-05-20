# *
# **
# ***

# def pattern(num):
#     for i in range(1,num): #1,num num=no of rows
#         for j in range(i,num):
#             print("*",end=" ")
#         print("\r")
# pattern(5)


#
# def pattern(num):
#     for i in range(0,num): #1,num num=no of rows
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print("\r")
# pattern(5)


# def pattern(num):
#     k=2*num-2
#     for i in range(0,num): #1,num num=no of rows
#         for j in range(0,k):
#                  print(end=" ")
#         k=k-1
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print("\r")
# pattern(5)



a="luminar"
b=input("enter a value")
flag=0
for i in a:
    if i in b:
       flag=1
if(flag==1):
    print("presnt")
else:
    print("not")


