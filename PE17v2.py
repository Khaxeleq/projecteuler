number=[]
engnum=[]
engnum1 = {'0': '', '1':'one' , '2':'two' , '3' : 'three', '4': 'four', '5':'five'
             ,'6':'six', '7': 'seven','8':'eight', '9':'nine'} 
engnum2 = {'10':'ten','11':'eleven','12':'twelve','13':'thirteen','14':'fourteen',
              '15':'fifteen','16':'sixteen','17':'seventeen','18':'eighteen',
              '19':'nineteen', '20':'twenty','30':'thrity','40':'forty', '50':'fifty',
              '60':'sixty','70':'seventy','80':'eighty','90':'ninety'}

a='and'
h = 'hundred'

for i in range(1,1000):
    number.append(str(i))

for i in number:
    if len(i)==3:
        engnum.append(h)
        engnum.append(engnum1[i[0]])
        if i[1:3] != '00':
            engnum.append(a)
            if i[1] == '1':
                engnum.append(engnum2[i[1:3]])
            elif i[1] == '0':
                engnum.append(engnum1[i[2]])
            else :
                engnum.append(engnum2[i[1]+'0'])
                engnum.append(engnum1[i[2]])
                
    elif len(i) == 2:
        if i[0] !='1':
            engnum.append(engnum2[i[0]+'0'])
            engnum.append(engnum1[i[1]])
        else :
            engnum.append(engnum2[i])
    elif len(i) == 1:
        engnum.append(engnum1[i])

allnumbers = ''.join(engnum)

print(len(allnumbers)+11)
        
        


