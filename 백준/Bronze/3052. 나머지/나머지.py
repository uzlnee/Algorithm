ans = []
for num in range(10):
    num = int(input())
    num %= 42
    ans.append(num) 

ans_uniq = list(set(ans))
print(len(ans_uniq))