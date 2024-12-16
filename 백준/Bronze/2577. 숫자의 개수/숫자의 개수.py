a = int(input())
b = int(input())
c = int(input())

abc = a * b * c
abc = str(abc)

arr = [0 for _ in range(10)]

for i in abc:
    arr[int(i)] += 1

for ans in arr:
    print(ans)
