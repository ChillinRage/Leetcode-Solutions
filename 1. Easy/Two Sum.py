def twoSum(nums, target):
    for i in range(len(nums)):
        if (target - nums[i]) in nums[i+1:]:
            second = target - nums[i]
            nums[i] += 1 # if both elements are similar
            return [i,nums.index(second)]
