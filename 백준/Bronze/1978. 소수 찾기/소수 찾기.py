n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for i in lst:
    for a in range(2, i+1):
        if i % a == 0:
            if i == a:
                cnt += 1
            break

print(cnt)