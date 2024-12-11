import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    p, h = map(int, input().split())
    arr.append([p, h])
arr.sort()

answer = 0
# 가장 높은 기둥 위치 찾기
i = 0
for a in arr:
    if a[1] > answer:
        answer = a[1]
        idx = i
    i += 1

# 왼쪽
height = arr[0][1]
for i in range(idx):
    if height < arr[i+1][1]:
        answer += height * (arr[i+1][0] - arr[i][0])
        height = arr[i+1][1]
    else:
        answer += height * (arr[i+1][0] - arr[i][0])

# 오른쪽
height = arr[-1][1]
for i in range(N-1, idx, -1):
    if height < arr[i-1][1]:
        answer += height * (arr[i][0] - arr[i-1][0])
        height = arr[i-1][1]
    else:
        answer += height * (arr[i][0] - arr[i-1][0])

print(answer)


