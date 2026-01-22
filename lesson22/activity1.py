def numberOfBits(n):
    ones=0
    zeros=0
    while(n):
        if(n&1==1):
            ones+=1
        else:
            zeros+=1
        n>>=1
    print("\n\nOnes=",ones,"\nzeros=",zeros)
number=int(input("enter your number:"))
numberOfBits(number)                