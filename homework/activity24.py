def reverse_binary(n):
    binary = bin(n)[2:]      
    rev_binary = binary[::-1]  
    rev_decimal = int(rev_binary, 2)  
    return binary, rev_binary, rev_decimal


num = int(input("Enter your original number: "))
b, rb, rd = reverse_binary(num)

print(f"Original Number (Binary): {b}")
print(f"Reversed Number : {rd} ({rb})")
