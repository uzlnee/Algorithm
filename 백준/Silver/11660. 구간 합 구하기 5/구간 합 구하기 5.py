import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for i in range(N):
    a = list(map(int, input().split()))
    arr.append(a)

prefix = [[0]*(N+1) for i in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix[i][j] = prefix[i][j-1] + prefix[i-1][j] - prefix[i-1][j-1] + arr[i-1][j-1]

for k in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    answer = prefix[x2][y2] - prefix[x2][y1-1] - prefix[x1-1][y2] + prefix[x1-1][y1-1]
    print(answer)