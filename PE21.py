import math as m
def divsum(num):
    divsum = 1
    x = 2
    while x<m.floor(m.sqrt(num)):
        if num%x == 0:
            divsum += x
            divsum += (num/x)

        x+=1
    return int(divsum)

amsum = 0
nums = []
for i in range (2,10001):
    nums.append(i)

while len(nums)>0:
    x = nums[0]
    y = divsum(x)
    z = divsum(y)
    nums.remove(x)
    if x == z and y<10000 and x != y:
        amsum+=(x+y)
        nums.remove(y)

print(amsum)
