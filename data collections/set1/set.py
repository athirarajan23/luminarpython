# s={1,5,4,9}   #doesnt keep your order
# print(s)

#
# a="abc"
# print(type(a))    #string type
#
# a=12
# print(type(a))
#
# a=True
# print(type(a))

#SET         SUPPORTS DIFF TYPE OF DATA
# empty set
# s=set()  #set()  is an empty set,also{} defines a dictionary
# print(s)
# print(type(s))
# s.add(9)
# s.add("hello")
# s.add(0.7)
# s.add(True)
# print(s)


#set doent support duplication elements

s1=set()
size=int(input("enter an input size"))
for i in range(size):
    element=int(input("enter a number"))
    s1.add(element)
print(s1)




