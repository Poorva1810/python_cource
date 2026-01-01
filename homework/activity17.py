def first_loop(n):
    for i in range(0, n + 1):
      print("Time Complexity: O(n)\n")

def second_loop(n):
    j = 1
    while j <= n + 1:
        j = j * 2
    print("Time Complexity: O(log n)\n")

def myfunction(n):
      print("Time Complexity for (0,100) is : O(1)")

n = 0
first_loop(n)
second_loop(n)
myfunction(n)
