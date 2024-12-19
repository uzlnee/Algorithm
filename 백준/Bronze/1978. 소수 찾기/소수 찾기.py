n = int(input())
lst = list(map(int, input().split()))

cnt = 0
for i in lst:
    rmd = []
    if i > 1:
        for a in range(2, i):
            b = i % a
            rmd.append(b)
        if 0 not in rmd:
            cnt += 1

print(cnt)