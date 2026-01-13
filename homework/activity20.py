a = int(input("Enter your smallest number: "))
b = int(input("Enter your largest number: "))
lcm = b
while True:
    if lcm % a == 0 and lcm % b == 0:
        print("LCM is:", lcm)
        break
    lcm += b
 