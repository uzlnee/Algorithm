N, M = map(int, input().split()) # 차례대로 전구와 명령어의 개수 입력
stat_arr = list(map(int, input().split())) # 전구의 상태 입력

# 전구 제어 명령어 구문
for i in range(M):
    a, b, c = map(int, input().split())
    if a == 1:
        stat_arr[b-1] = c
    elif a == 2:
        for j in range(b-1, c):
            if stat_arr[j] == 0:
                stat_arr[j] = 1
            else:
                stat_arr[j] = 0
    elif a == 3:
        for j in range(b-1, c):
            stat_arr[j] = 0
    else:
        for j in range(b-1, c):
            stat_arr[j] = 1

for i in range(N):
    print(stat_arr[i], end=' ')