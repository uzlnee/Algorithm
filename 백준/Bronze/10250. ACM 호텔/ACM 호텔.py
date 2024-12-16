T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    if N % H == 0:
        floor = str(H)
        id = N // H
        if id < 10:
            print(floor + "0" + str(id))
        else:
            print(floor + str(id))
    else:
        floor = str(N % H)
        id = N // H + 1
        if id < 10:
            print(floor + "0" + str(id))
        else:
            print(floor + str(id))

