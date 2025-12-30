def multiply_iterative(n, m):
    result = 1
    for i in range(n, m + 1):
        result *= i
    return result
def multiply_recursive(n, m):
    if n > m:
        return 1
    return n * multiply_recursive(n + 1, m)
n = int(input("Enter starting number (N): "))
m = int(input("Enter ending number (M): "))

print("Multiplication using iteration:", multiply_iterative(n, m))
print("Multiplication using recursion:", multiply_recursive(n, m))
    