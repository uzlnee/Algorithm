n, k = map(int, input().split())

ja = 1
mo1 = 1
mo2 = 1
for i in range(n, 0, -1):
    ja *= i

for i in range(k, 0, -1):
    mo1 *= i

for i in range(n-k, 0, -1):
    mo2 *= i

result = ja / (mo1 * mo2)
print(int(result))