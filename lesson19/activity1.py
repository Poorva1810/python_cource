n=int(input("enter your number"))
number=n
reverse=0
while (n>0):
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if number==reverse:
    print("it is palindrome number")
else:
    print("it is not palindrome number")        