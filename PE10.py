primes=[2]


x=3
while len(primes)<10:
   for y in range(2,x):
       if x%y==0:
           x+=1
   primes.append(x)
   x+=1
print(primes)   
