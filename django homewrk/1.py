lst=[7,8,9,4,3,1]
# op=[]
# for num in lst:
#     if num>5:
#         op.append((num+1))
#     else:
#         op.append((num-1))
# print(op)
#using map function the code can be written in to single code
op=list(map(lambda num:num+1 if num>5 else num-1,lst))
print(op)