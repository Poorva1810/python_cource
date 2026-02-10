s = input("Enter string: ")
n = len(s)
for i in range(n):
    for j in range(i + 1, n + 1):
        print(s[i:j])
