# number=[x for x in range(20) if x%2!=0]   #odd numbers
# print(number)


# number_list=[x for x in range(25) if x%2==0]   #even numbers
# print(number_list)


# ar=[2,3,4,5,6] # square of numbers
# square=[num**2 for num in ar]
# print(square)


# fruits=["mango","orange","grape"]
# pair=[(fruit,fruit) for fruit in fruits]
# print(pair)

# lst1=[1,2]
# lst2=[10,20] # output as [(1,10),(1,20),(2,10),(2,20)]
# pairs=[(num1,num2) for num1 in lst1 for num2 in lst2]
# print(pairs)

lst2=[10,11,12,13,14]          #evens
evens=[num for num in lst2 if num%2==0]
print(evens)

pattern=[num+1 if num>5 else num-1 for num in lst2]  #ascending order
print(pattern)

