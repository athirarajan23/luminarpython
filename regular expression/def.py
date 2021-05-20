#pattern matching

#re---package for pattern matching


# import re
# count = 0
# matcher=re.finditer('ab','abaaabbab')   #insted of loop finditer method can be used
# for match in matcher:
#     count+=1
# print("count=",count)



import re
count = 0
matcher=re.finditer('ab','abaaabbab')   #insted of loop finditer method can be used
for match in matcher:
    print("match available at",match.start())  #start is used to return position
    print("group=",match.group())
    count+=1
print("count=",count)