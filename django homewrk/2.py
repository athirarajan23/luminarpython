lst=[10,20,21,22,23]
lst2=[20,21,10,22,23]
lst.sort()
lst2.sort()
if(lst==lst2):
    print("equal")
else:
    print("not equal")

# compare=lambda lst,lst2:len(lst)==len(lst2) and len(lst)==sum([1 for i,j in zip(lst,lst2) if i==j])