#count char in given string
#eg hello: l: 2
char=input("enter a character")
a="helloooo"
count=0
for i in a:   #i is for ==
    if i in char:
        count+=1
print(count)

