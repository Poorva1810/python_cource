from math import sqrt
n=int(input("enter your number"))
if n>1:
    isprime=True
    for i in range(2,int(sqrt(n))+1):
        if(n%i)==0:
         isprime=False
         break
    if isprime:
       print("prime number")
    else:
       print("not a prime number")   
else:
   print("not a prime number")           
