a=input("enter a string")
count=0
vowels="aeiou"
for i in a:
    if i in vowels:
        count+=1
print(count)
