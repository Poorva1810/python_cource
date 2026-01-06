def factors(number):
    print("the factors are")
    for i in range(1,number+1):
        if number%i==0:
            print(i)
number=int(input("enter your number"))
factors(number)            
