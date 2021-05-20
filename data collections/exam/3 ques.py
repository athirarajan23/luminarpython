# list1 = [3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
# max = max(list1[0], list1[1])
# secondmax = min(list1[0], list1[1])
# n = len(list1)
# for i in range(2, n):
#     if list1[i] > max:
#         secondmax = max
#         max = list1[i]
#     elif list1[i] > secondmax and max != list1[i]:
#         secondmax = list1[i]
# print("Second highest number is : ",str(secondmax))

#another way
list1 = [3,5,7,9,0,8,55,34,23,76,4,65,12,89,56,76,34,289,49,12,63,976]
list1.sort()
print(list1[-2])  # - is given to find 2 lar