
def rev(string):
    string2=""
    for x in range(len(string)):
        string2=string2+(string[len(string)-(x+1)])
    return (string2)

print(rev("2345"))

palindromes=[]
for x in range(100,999):
    for y in range(100,999):
        z=x*y
        w=str(z)
        if w == rev(w):
            palindromes.append(int(w))
print(max(palindromes))
