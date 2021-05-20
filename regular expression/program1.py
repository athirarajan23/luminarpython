import re
n="hello"   #special symbols invalid
x="\w*"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")