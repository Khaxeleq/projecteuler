numbers="7595 6417 47 8218 35 87 1020 04 82 47 6519 01 23 75 03 3488 02 77 73 07 63 6799 65 04 28 06 16 70 9241 41 26 56 83 40 80 70 3341 48 72 33 47 32 37 16 94 2953 71 44 65 25 43 91 52 97 51 1470 11 33 28 77 73 17 78 39 68 17 5791 71 52 38 17 14 91 43 58 50 27 29 4863 66 04 68 89 53 67 30 73 16 69 87 40 3104 62 98 27 23 09 70 98 73 93 38 53 60 04 23"
def delblank(string):
    newstring=string.replace(" ","")        
    return newstring
numbers1=delblank(numbers)
numlist=[]

for i in range(0,len(numbers1),2):
    numlist.append(int(numbers1[i]+numbers1[i+1]))


tierlist=[]

k=0
n=1
while k< 16*7.5:
    tierlist.append(numlist[k:k+n])
    k=k+n
    n+=1



for i in range(13,-1,-1):
    for j in range(i,-1,-1):
        a=tierlist[i+1][j+1]
        b=tierlist[i+1][j]
        if a>b:
            tierlist[i][j]=a+tierlist[i][j]
        if b>a:
            tierlist[i][j]=b+tierlist[i][j]
print(tierlist)
    

    

