def term(number):
    if number==1:
        return 0
    elif number==2:
        return 1
    else:
        return term(number-1)+term(number-2)
number=int(input("enter the number of term of fibonacci series"))
if number<=0:
    print("series dose not axist for negative number")
else:
    print("the term of the series is",term(number))

    
