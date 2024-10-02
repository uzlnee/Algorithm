# 테스트 케이스 개수
n_case = int(input())


# 입력/출력
for i in range(n_case):
    n_test = int(input())
    arr = list(map(int, input().split()))
    print(min(arr), max(arr))