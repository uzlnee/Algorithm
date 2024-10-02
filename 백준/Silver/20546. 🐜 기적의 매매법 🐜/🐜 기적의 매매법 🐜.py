cash = int(input())
machineduck = list(map(int, input().split()))

jh = cash
sm = cash
jh_stock = 0
sm_stock = 0

# 준현
for i in machineduck:
    if jh < i:
        continue
    else:
        jh_stock += jh // i
        jh = jh % i
jh_sum = jh + (jh_stock * machineduck[-1])

# 성민
for i in range(3, 14):
    # 매수
    if machineduck[i-3] > machineduck[i-2] > machineduck[i-1] > machineduck[i]:
        sm_stock += sm // machineduck[i]
        sm = sm % machineduck[i]

    # 매도
    elif machineduck[i-3] < machineduck[i-2] < machineduck[i-1] < machineduck[i]:
        sm += sm_stock * machineduck[i]
        sm_stock = 0
sm_sum = sm + (sm_stock * machineduck[-1])        

if jh_sum > sm_sum:
    print('BNP')
elif jh_sum < sm_sum:
    print('TIMING')
else:
    print('SAMESAME')