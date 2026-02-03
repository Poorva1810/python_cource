import math

def f1(s,size):

  psize=(int)(math.pow(2,size))

x=0

y=0

for x in range(psize):#8

 for y in range(size):#3

  if((x&(1<<y))>0):

   print([y],end="")

print("")

size=int(input("Enter array size: "))

set=[]

for i in range(size):

  n=input("Enter an element : ")

set.append(n)

f1(set,len(set))
