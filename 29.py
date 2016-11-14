nums = {}

for i in range(2,101):
    for j in range(2,101):
        try:
            dummy = nums[i**j]
        except KeyError:
            nums[i**j] = True

print len(nums.keys())
