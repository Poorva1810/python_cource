n=int(input("enter your smallest number"))
m=int(input("enter your largest number"))
while(n):
    sn=n
    n=m%n
    m=sn
print("hcf is:",m)    