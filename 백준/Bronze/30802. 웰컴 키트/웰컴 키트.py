N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

t_cnt = 0
for s in size:
    if s == 0:
        continue
    elif s <= T:
        t_cnt += 1
    elif s%T==0:
        t_cnt += s//T
    else:
        t_cnt += s//T+1

print(t_cnt)
print(N//P, N%P)