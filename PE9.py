import math


for a in range(1,1000):
    for b in range(1,1000):
        c=a**2+b**2
        if math.sqrt(c)+a+b==1000:
            d=a*b*math.sqrt(c)
            print(a)
            print(b)
            print(math.sqrt(c))
            print(d)
            break
