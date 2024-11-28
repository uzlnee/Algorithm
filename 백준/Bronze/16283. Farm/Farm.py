a, b, n, w = map(int, input().split())

cnt = 0
ans = []
for sheep in range(1, n):
    cow = n - sheep
    if (w == (sheep*a) + (cow*b)):
        ans.append((sheep, cow))
        cnt += 1

if cnt == 1:
    print(*ans[0])
else:
    print(-1)