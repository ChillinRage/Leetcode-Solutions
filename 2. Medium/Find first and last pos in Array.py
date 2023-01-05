def searchRange(nums, target):
    if not nums:
        return [-1,-1]
    
    low, high = 0, len(nums)-1
    
    while low < high:
        mid = (low+high)//2
        
        if nums[mid] == target:
            high = mid 
        elif nums[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
            
    if nums[low] != target:
        return [-1,-1]
    
    output = [low]
    
    while low < len(nums) and nums[low] == target:
        low += 1
        
    return output+[low-1]
