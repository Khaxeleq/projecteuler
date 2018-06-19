numbers=[]
##this the list of numbers
verticalsums=[]
##these are all the possible sums that can be taken vertically.
for i in range(0,341):
    verticalsums.append(numbers[i]*numbers[i+20]*numbers[i+40]*numbers[i+60])


horizontalsums=[]
##all possible horizontal sums
for j in range(0,397):
    if 20%(j+20)<16:
        horizontalsums.append(numbers[j]*numbers[j+1]*numbers[j+2]*numbers[j+3])


diagonal1sums=[]
##all possible sums diagonal top left to bottom right

for k in range(0,341):
    if 20%(k+20)<17:
        diagonal1sums.append(numbers[k]*numbers[k+21]*numbers[k+42]*numbers[k+63])


diagonal2sums=[]
##all possible diagonal sums bottom left to top right
for l in range(0,341):
    if 20%(l+20)>3:
        diagonal2sums.append(numbers[l]*numbers[l+19]*numbers[l+38]*numbers[l+57])


##the list containing all lists
allsums=verticalsums+horizontalsums+diagonal1sums+diagonal2sums
print(max(allsums))
    
