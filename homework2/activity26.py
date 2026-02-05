n = int(input("Enter your number: "))
count = 0
while n != 0:
    n = n & (n << 1)
    count += 1
print("Longest consecutive 1’s length :", count)