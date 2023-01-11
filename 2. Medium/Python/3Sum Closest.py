def threeSumClosest(nums, target):
    def twoSumClosest(nums, target):
        low, high  = 0, len(nums) - 1
        close      = nums[low] + nums[high]
            
        while low < high:
            if nums[low] + nums[high] == target:  # sum equals target
                return target
                
            sum_diff   = abs(target - (nums[low] + nums[high]))
            close_diff = abs(target - close)
                
            if sum_diff < close_diff:
                close = nums[low] + nums[high]
                    
            if target > (nums[low] + nums[high]):
                low += 1
            else:
                high -= 1
            
        return close
        
    nums.sort()
    closest = 10**5
    
    for i in range(len(nums) - 2):
        diff    = target - nums[i]
        close = twoSumClosest(nums[i + 1:], diff)
        if abs(target - closest) > abs(target - (close + nums[i])):
            closest = close + nums[i]
        
    return closest
