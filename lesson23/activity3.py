

n=int(input("How many elements in the array? "))#8

ar=[]

i=1

while i<=n:

 x=int(input('Enter a number : '))

ar.append(x)

i+=1

x2=ar[0]

x=0

y=0

b=0

for i in range(1,n):

 x2=x2^ar[i]

b=x2 & ~(x2-1)

for i in range(n):

 if ar[i]&b:#ar[i] is also having 1 at the first set bit position, 30 has 1 at position 2

  x=x^ar[i]

else:

 y=y^ar[i]

print("The two odd occuring elements are :",x,"and",y)