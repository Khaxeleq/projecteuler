def collatz(n):
    count=1
    while n!=1:
        if n%2==1:
            n=3*n+1
        else :
            n=n/2
    
    
        count+=1
    return count

##m=1
##goldy=1
##for i in range(1,1000000):
##    q = collatz(i)
##    if q>m:
##        m=q
##        goldy=i
##    
##
##print(goldy)

sequen={}

for i in range (1,1000000):
    sequen={i:collatz(i)}


