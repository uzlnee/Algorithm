num = list(map(int, input().split()))

sum = 0
for n in num:
    sum += n**2
    
answer = sum % 10
print(answer)
    