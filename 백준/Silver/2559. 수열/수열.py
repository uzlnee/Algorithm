N, K = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0 for _ in range(N+1)]

for i in range(N):
    prefix[i+1] = prefix[i] + arr[i]

answer = []
for k in range(K, N+1):
    answer.append(prefix[k] - prefix[k-K])

print(max(answer))