money = int(input())
tax = 0
if money < 15528:
  tax = 15
elif money < 42708:
  tax = 25
elif money > 132406:
  tax = 28
  nums = [n for n in range(20)]
print(nums)
print(nums[2:5])
name = 'Python is not a snake'
print(name[7:0:-1])

nums = [n * 2 for n in range(1, 21)]
print(nums)
print(nums[2:7])

str1 = 'Python is not just a mere snake'
print(str1[10:18])

print(str1[::-1])
print(str1[7::])

new_str = str1[:]
print(new_str)

my_list = ['Java', 'Python', 'Kotlin']
print(my_list[:2])
print(my_list[:99999999])