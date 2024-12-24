n, m = map(int, input().split())
cards = list(map(int, input().split()))
cards.sort()

answer = 0
for a in range(n):
    for b in range(a+1, n):
        for c in range(b+1, n):
            result = cards[a] + cards[b] + cards[c]
            if result > m:
                continue
            else:
                answer = max(answer, result)

print(answer)