a=int(input("enter a: "))
b=int(input("enter b: "))
print("the numbers before swapping: a=",a,"b=",b)
a,b=b,a
print("the numbers after swapping: a= ",a,"b=",b)
def swap1(a,b):
    print("before swapping: ",a,b)
    a=a+b
    b=a-b
    a=a-b
    print("after swapping:",a,b)
def swap2(a,b):
    print("beforeswapping:",a,b)
    a=a^b
    b=a^b
    a=a^b
    print("after swapping:",a,b)
def swap3(a,b):
    print("before swapping",a,b)
    a=(a&b)+(a|b)
    b=a+(~b)+1
    a=a+(~b)+1
    print("after swapping",a,b)        
'''

1100 , 0101

a&b =1100 & 0101= 0100

a|b =1100 | 0101 =1101

a= (a&b)+(a|b) =10001

b=a+(~b)+1=10001

+01010

+00001

b= 11100

0+0=0, 0+1=1, 1+1=10, 1+1+1=11

a=a+(~b)+1=10001

+00011

+00001

10101

'''
swap1(30,40)
swap2(30,40)
swap3(30,40)   