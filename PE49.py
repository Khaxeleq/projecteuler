primes=[]
p=1001
while p<10000:
   i=1
   while i<p:
       i+=1
       if p%i==0:
           break
   if i==p:
      primes.append(p)
       
   p+=2

primedig = {}

for i in primes:
   



        
