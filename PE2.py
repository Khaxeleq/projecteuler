fib1=1
fib2=1
y=0
while fib1+fib2<4000000:
   fib3=fib1+fib2
   if fib3%2==0:
       y+=fib3
   fib1=fib2
   fib2=fib3
print(y)

   
