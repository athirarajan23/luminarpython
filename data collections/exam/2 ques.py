count={}
f=open("fil","r")
for n in f:
    words=n.split(" ")
    for word in words:
        if word not in count:
            count.update({word:1})
        else:
            val=int(count[word])
            val+=1
            count.update({word:val})
print(count)