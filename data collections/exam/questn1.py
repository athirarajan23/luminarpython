# a=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# duplicte_elements={1,0,7,5,9,2,3,5,7,2,0,1,10}
# unique_elements=[]
# for i in a:
#     if i in duplicte_elements:
#         unique_elements.append(i)
#         duplicte_elements.add(i)
# print(duplicte_elements)

#method to be used:
a=[1,0,7,5,9,2,3,5,7,2,0,1,10]
b=list(set(a))
print(b)