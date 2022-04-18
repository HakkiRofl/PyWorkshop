c = input().split(" ")
count = c[1]
nums = input().split(" ")
nums = [int(i) for i in nums]
i = j = 0
num = 0
while i < len(nums) and j < len(nums):
  if nums[j] - nums[i] < int(count):
    j += 1
  else:
    num += len(nums) - j
    i += 1
print(num)
