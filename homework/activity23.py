n = int(input("Enter number: "))
position = 1
while n > 0:
    if n & 1:
        print("Position of the first set bit: ", position)
        break
    n = n >> 1
    position += 1