def removeDuplicates(nums):
    count = 0
    i     = 0
        
    while (i < len(nums) - 1) and (nums[i] != ''):
        count += 1
        if nums[i] != nums[i + 1]:
            count = 0
                
        if count >= 2:
            nums.remove(nums[i])
        else:
            i = i + 1

    # no return because process is done in-place
