empty=dict()
for x in range(1,22):
    empty[(x,21)]=1
    empty[(21,x)]=1
    ways=empty
##print(ways)
for i in range(20,0):
    for j in range(20,0):
        ways[(i,j)]=ways[(i+1,j)]+ways[(i,j+1)] 
print(ways)        

