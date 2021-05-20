arr=[2,3,4,5,6]
#to find square
# def square(num):
#     return num**2
#in the case of map(function,iterable) we have to assign

squarelist=list(map(lambda num:num**2,arr))
print(squarelist)

#while giving lambda in to it removing def function
