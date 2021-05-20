numbers=[1,2,4,5,7,6]
prime=[]
non_prime=[]
for i in numbers:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                non_prime.append(i)
                break
        else:
            prime.append(i)
print("prime numbers are:",prime)
print("non_prime numbers are:",non_prime)