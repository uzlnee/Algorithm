N = int(input())

cnt = 0
for C in range(1, N-2):
    for B in range(1, N-2):
        for A in range(2, N-2):
            if (A+B+C==N) and (C>=B+2) and (A%2==0): # 2개 이상!!!
                cnt += 1

print(cnt)