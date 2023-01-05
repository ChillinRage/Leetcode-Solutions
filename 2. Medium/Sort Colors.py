# Solution 1: cheese strat
def sortColors1(nums):
    count = [0,0,0]
    
    for i in nums:
        count[i] += 1
        
    nums[:] = [0 for i in range(count[0])] + [1 for i in range(count[1])] + \
              [2 for i in range(count[2])]

# Solution 2: intended approach
def sortColors2(nums):
    low, mid, high = 0, 0, len(nums) - 1
        
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[high], nums[mid] = nums[mid], nums[high]
            high -= 1
