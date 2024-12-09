import sys

input = sys.stdin.readline
N, M = map(int, input().split())
n_list = list(map(int, input().split()))
prefix = [0]
sum = 0

for a in n_list:
    sum += a
    prefix.append(sum)

for _ in range(M):
    i, j = map(int, input().split())
    answer = prefix[j] - prefix[i-1]
    print(answer)