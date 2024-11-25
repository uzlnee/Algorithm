n = int(input())

cnt = 0
for i in range(1, 501):
    for j in range(i, 501):
        b = j*j
        if (b - (i*i) == n):
            cnt += 1
        elif (b - (i*i) > n):
            break
            
print(cnt)