num = int(input("Enter a number: "))
num_digits = len(str(num))
sum_of_powers = sum(int(digit) ** num_digits for digit in str(num))
if num == sum_of_powers:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
