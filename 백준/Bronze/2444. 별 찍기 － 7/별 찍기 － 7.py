n = int(input())

for i in range(1, n):
    print(" " * (n-i) + "*" * (2*i-1))

for i in range(n):
    k = i + (i+1)
    print(" " * i + "*" * (2*n-k))