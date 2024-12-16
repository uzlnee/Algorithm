T = int(input())

for i in range(T):
    res = input()
    answer = 0
    score = 0
    
    for r in res:
        if r == "O":
            score += 1
            answer += score
        else:
            score = 0
    print(answer)

