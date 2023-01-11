def missingNumber(nums):
    summ = sum(i for i in range(len(nums)+1))

    for n in nums:
        summ -= n
        
    return summ
