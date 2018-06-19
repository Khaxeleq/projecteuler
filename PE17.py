numo=[] 
numbers=[17]
##Both of these empty lists will be used later on

for i in range(1,1000):
    numbers.append(i)
##The list 'numbers' now contains all numbers from 1 to 999 inclusive.

count=0
##count represents the total number of letters
for j in numbers:
    numo.append(str(j))
##The list 'numo' contains all numbers in the list 'numbers', in string format

for j in numo:
    if len(j)==3:
        count+=7
    ##This section checks the length of a number as a string. If it is equal to three, it means the number contains 'hundred' when written, thus 7 must be added to 'count'.
        
        if j[1:3]!='00':
            count+=3
        ##If the figure of length three contains any non-zero tens or units, then the 'and'(i.e. '201' would be written as 'two hundred AND one') must be considered and thus 3 must be added to 'count'. 
counto=count
digits=[]
##Now that all 'hundred's and 'and's are accounted for, all numbers can be seperated into units and tens. 'digits' will contain all numbers that have unique spelling.

for i in numo:
    if len(i)==3:## Considering three digit numbers
        if i[1]=='1': ##Any teens will need to be considered seperately as they have distinct spellings.
            digits.append(i[0])
            digits.append(i[1:3])
        elif i[1] == '0': ##If the tens digit is zero then we only need to consider the hundreds and units
            digits.append(i[2])
            digits.append(i[0])
        elif i[1]!='0': ## If the tens digit is any other number besides 0 or 1, then the tens number must be considered seperately.
            digits.append(i[1]+'0')##This ensures the tens digit is not simply recorded as a unit would since, for example 'seventy' would otherwise be recorded as 'seven' which would be incorrect.
            digits.append(i[2])
            digits.append(i[0])
       
    elif len(i) == 2:## Considering two digit numbers
        if i[0]=='1':
            digits.append(i)
        else:
            
            digits.append(i[0]+'0')
            digits.append(i[1])
    else :## Considering single digit numbers
        digits.append(i)

nums=[]
for i in digits:
    if i != '0':
        nums.append(i)
## The list 'nums' is just equal to 'digits' except all '0's are removed
for j in nums:
    if len(j)==1:
        if j in [ '1', '2', '6']:
            count+=3
        elif j in ['3', '7', '8']:
            count+=5
        else:
            count+=4
    else:
        if j in [ '11', '12', '20', '30', '80', '90']:
            count+=6
        if j in [ '40', '50', '60']:
            count+=5
        if j in [ '15', '16', '70']:
            count+=7
        if j in [ '13', '14', '19', '18']:
            count+=8
        if j in [ '17']:
            count+=9
        if j == ['10']:
            count+=3
##All figures in nums are considered and the amount of letters in their english spellings are added to 'count'.            
count+=11 ## Incorporating '1000' would have been a pain so I just did it myself.

print(count)
    

