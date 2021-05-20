numbers={1,2,4,5,7,6}
prime=set()
non_prime=set()
for i in numbers:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                non_prime.add(i)
                break
        else:
            prime.add(i)
print("prime numbers are:",prime)
print("non_prime numbers are:",non_prime)

