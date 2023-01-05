def thirdMax(nums):
    nums = list(set(nums))
    
    if len(nums) <= 2:
        return nums[-1]
    else:
        return sorted(nums)[-3]
