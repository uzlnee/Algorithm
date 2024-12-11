n, x = map(int, input().split())
arr = list(map(int, input().split()))

answer = []
for a in arr:
    if a < x:
        answer.append(a)

print(*answer)