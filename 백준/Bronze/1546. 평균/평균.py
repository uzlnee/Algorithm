n = int(input())
scores = list(map(int, input().split()))

scores.sort()
maxi = max(scores)

new_scores = []
for s in scores:
    s = s / maxi * 100
    new_scores.append(s)

mean_score = sum(new_scores) / n
print(mean_score)