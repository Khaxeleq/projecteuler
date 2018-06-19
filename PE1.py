def sum_of_two_multiples(num1,num2,limit):
    x=0
    for y in range(limit):
        if y%num1 == 0 or y%num2 == 0:
            x+=y
    return(x)
t=sum_of_two_multiples(3,5,1000)
print(t)
    


