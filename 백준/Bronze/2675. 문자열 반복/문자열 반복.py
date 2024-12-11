T = int(input())

for _ in range(T):
    r, s = input().split()
    for i in range(len(s)):
        print(int(r) * s[i], end='')
    print()