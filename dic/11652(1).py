import sys

N = int(sys.stdin.readline())
nums = {}
for _ in range(N):
    num = int(sys.stdin.readline())
    if num not in nums:
        nums[num] = 1
    else:
        nums[num] +=1
nums = sorted(nums.items(), key = lambda x: (x[1], -x[0]))

print(nums)
print(nums[-1][0])