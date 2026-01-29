def f1(n):
    if n==0:
        return 0
    if (n&(n-1)==0):
        return 1
    return 0
n=int(input("enter a number"))
if f1(n):
    print(n,"is power of 2")
else:
    print("n,is not power of 2") 

n=int(input("enter a number"))
m=n
if n==0:
    print(m,"is not power of 2")
else:
    while n%m==0:
        n=n/2
    if n==1:
        print(m,"is power of 2")
    else:
        print(m,"is not power of 2")            