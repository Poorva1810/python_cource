def isevenodd(n):
    if(n^1==n+1):
        return True
    else:
        return False
n=int(input("enter your number: "))
if isevenodd(n):
    print("even number")
else:
    print("odd number")        
        
    