def nd( day ):
    nd = 0
    if day == 'M':
        nd = 'Tu'
    elif day == 'Tu':
        nd = 'W'
    elif day == 'W':
        nd = 'Th'
    elif day == 'Th':
        nd = 'F'
    elif day == 'F':
        nd = 'Sa'
    elif day == 'Sa':
        nd = 'Su'
    else:
        nd = 'M'
    return nd

year = 1900
months = []
nyear = [31,28,31,30,31,30,31,31,30,31,30,31]
lyear = [31,29,31,30,31,30,31,31,30,31,30,31]
days = []
Mcount = 0
Tucount = 0
Wcount = 0
Thcount = 0
Fcount = 0
Sacount =0
Sucount = 0
day = 'M'
ymonth = 0
month=[]
while year<2001:
    if year%100 == 0:
        if year %400 == 0:
            months = lyear
        else :
            months = nyear
    else:
        if year%4 == 0:
            months = lyear
        else:
            months = nyear
   
    while ymonth <12:
        month.append(day)
        day = nd(day)
        if len(month) == months[ymonth]:
            if year>1900:
                m = month[0]
                if m =='Su':
                    Sucount+=1
                elif m == 'M':
                    Mcount+=1
                elif m == 'Tu':
                    Tucount+=1
                elif m == 'W':
                    Wcount+=1
                elif m == 'Th':
                    Thcount+=1
                elif m == 'F':
                    Fcount +=1
                else:
                    Sacount+=1
                    
            month = []
            ymonth+=1
    year+=1
    ymonth = 0

allcounts = [ Mcount, Tucount, Wcount, Thcount, Fcount, Sacount, Sucount]
print(allcounts)
    
        
    
    
    
        
