n = int(input("Enter your number: "))
original = n
if n > 0:
    while n % 8 == 0:
        n = n // 8
    if n == 1:
        print(f"no {original} is not  the power of 8")
    else:
        print(f"yes  {original} is  the power of 8")
else:
    print(f"yes  {original} is the power of 8")