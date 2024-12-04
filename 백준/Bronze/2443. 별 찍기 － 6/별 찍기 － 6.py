n = int(input())

for i in range(n):
    k = i + (i+1)
    print(" " * i + "*" * (2*n-k))