n=int(input("how many elements in the array?"))
ar=[]
i=1
while i<=n:
    x=int(input("enter a number:"))
    ar.append(x)
    i+1
res=0
for x in ar:
    res=res^x
print(res,"is odd occuring number in array",ar)        