def threeSum(nums):
    if len(nums) < 3:
        return []
        
    output = []
    nums.sort()
    
    for i in range(len(nums)-2):
        j = i+1
        k = len(nums)-1
        
        while j < k:
            if nums[i]+nums[j]+nums[k] == 0:
                if [nums[i],nums[j],nums[k]] not in output:
                    output.append([nums[i],nums[j],nums[k]])    
                j += 1
                
            elif abs(nums[i]+nums[j]) > nums[k]:
                j += 1
                
            else:
                k -= 1
                
    return output
