n = int(input())
nums = list(map(int, input().split()))

min = nums[0]
max = nums[0]
for number in nums:
    if number < min:
        min = number
    elif number > max:
        max = number
print(min, max)