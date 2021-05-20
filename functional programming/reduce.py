#single output will be there in reduce
arr=[1,2,3,4,5,6]
#to find sum of the above list
from functools import reduce
# total=reduce(lambda num1,num2:num1+num2,arr)
# print(total)
# highest number in the list
highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr)
print(highest)