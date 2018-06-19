##
##list2=[]
##q=0
##while q<20:
##    list2.append(0)
##    q+=1



    


for i in range(21,1000000000):
    list1=[]
    for x in range(1,21):
        if i%x == 0:
            list1.append(x)
            if len(list1)==20:
               print(i)
##        
##x=1
##l1=[]
##while x<21:
##    l1.append(x)
##    x+=1
##print(l1)
##
##for y in l1:
##    for i in range(21,100000000000):
##        z=i%y
##        if z!=0:
##            continue
##    
##    print(i)
##    break
##    
   
    
