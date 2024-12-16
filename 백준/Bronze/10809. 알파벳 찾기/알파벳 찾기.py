stri = input()

arr = [-1 for _ in range(26)]

for i in range(len(stri)):
    alp = ord(stri[i]) - 97
    if arr[alp] == -1:
        arr[alp] = i

print(*arr)