a=input("enter a string")
b=""
symbols="!@#$%^&*+*-/|?<>:{}()"
for i in a:
    if i not in symbols:
        b+=i
print(b)
