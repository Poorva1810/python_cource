def f1(n):
    c=0
    if(n&(n-1))!=0:
        while n>1:
            n=n>>1
            c+=1
    if c%2==0:
        return 1
    else:
        return 0
num=int(input("enter a number"))
if f1(num):
    print(num,"is a power of 4")
else:
    print(num,"is not power of 4")


