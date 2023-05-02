nums = []

nums2 = [6, 7, 8, 9, 10]

nums.append(1)
nums.append(2)
nums.append(3)
nums.append(4)
nums.append(5)



for i in range(0, len(nums)):
    print(nums[i])


nums += nums2

for i in range(0, len(nums)):
    print(nums[i])
    

nums = sorted(nums, reverse=True)

print(nums)