n = int(input())

hints = [list(map(str, input().split())) for _ in range(n)]
answer = 0

for a in range(1, 10):  # 100의 자리수 (1~9)
    for b in range(1, 10):  # 10의 자리수 (1~9)
        for c in range(1, 10):  # 1의 자리수 (1~9)
            if (a == b or b == c or c == a):
                continue

            valid = True
            for hint in hints:
                num = hint[0]  
                strike = int(hint[1]) 
                ball = int(hint[2])  

                strike_cnt = 0
                ball_cnt = 0

                if a == int(num[0]):
                    strike_cnt += 1
                if b == int(num[1]):
                    strike_cnt += 1
                if c == int(num[2]):
                    strike_cnt += 1

                if a == int(num[1]) or a == int(num[2]):
                    ball_cnt += 1
                if b == int(num[0]) or b == int(num[2]):
                    ball_cnt += 1
                if c == int(num[0]) or c == int(num[1]):
                    ball_cnt += 1

                if strike != strike_cnt or ball != ball_cnt:
                    valid = False
                    break

            if valid:
                answer += 1

print(answer)
