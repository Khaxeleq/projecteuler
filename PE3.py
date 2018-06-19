factors=[]
x=1
y=600851475143
for x in range(1,2000):
    if y%x != 0:
        continue
    elif y%x == 0:
        y= y/x
        x=0
        continue    
print(y)        
    

    
