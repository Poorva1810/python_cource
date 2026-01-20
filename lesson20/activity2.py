def sieve(n):
    prime=[True for i in range(n+1)]
    p=2
    while(p*p<=n):
        if prime[p]==True:
            for i in range(p*p,n+1,p):
                prime[i]=False
        p=p+1
    for p in range(2,n+1):
        if prime[p]:
            print(p)
n=int(input("enter your number"))
print("following are the prime number smaller"),
print("than or equal to",n)
sieve(n)                        
