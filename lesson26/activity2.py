import math
def f1(s,size):
    psize=int(math.pow(2,size))
    x=0
    y=0
    for x in range(psize):
        for y in range(size):
            if((x&(1<<y))>0):
                print(s[y],end="")
        print("")
size=int(input("enter array size :"))
set=[]
for i in range(size):
    n=input("enter an element")
    set.append(n)
f1(set,len(set))
                    