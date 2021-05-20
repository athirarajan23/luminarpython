# a function calling itself is reccursion
def recur_feb(n):
    if n<=1:
        return n
    else:
        return recur_feb(n-1)+recur_feb(n-2)
nterms=10
if nterms<=0:
    print("enter a positive integer")
else:
    print("febinocci sequence:")
    for i in range(nterms):
        print(recur_feb(i))