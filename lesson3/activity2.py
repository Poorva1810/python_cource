def factorial(number):
    if number==1:
        return number
    else:
        return number*factorial(number-1)
number=int(input("enter the number to calculate factorial"))
if number<0:
    print("factorial does not axist for nagetive numbers")
elif number==0:
    print("the factorial of 0 is 1")
else:
    print("factorial is ",factorial(number))        
