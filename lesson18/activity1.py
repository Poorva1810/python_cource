number=int(input("enter your number"))
length=len(str(number))
result=0
temp=number
while temp>0:
    digit=temp%10
    result=result+digit**length
    temp=temp//10
if number==result:
    print("armstrong number")
else:
    print("not an armstrong number")        