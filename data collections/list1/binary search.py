#spliting list in to 2parts using middle term
list=[2,34,4,5,3,9,55,41,31,8]

def binarysearch():
    list.sort()
    print(list)
    ele=int(input("enter the element"))
    fla=0
    min=0
    max=len(list)-1
    while(min<=max):
        mid=(min+max)//2
        if ele>list[mid]:
            min=mid+1
        elif ele<list[mid]:
            max=mid-1
        elif ele==list[mid]:
            fla=1
            break
    if fla==1:
        print("found")
    else:
        print("not found")
binarysearch()





