def setOrNot(number,n):
    if number&(1<<(n-1)):
        print("\nSET")
    else:
        print("\nNOT SET")
number=int(input("enter number:"))
n=int(input("enter bit number:"))
setOrNot(number,n)            