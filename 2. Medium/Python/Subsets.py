def subsets(nums):
    if not nums:
        return [[]]
        
    current = nums[0]
    previous = subsets(nums[1:])
    length = len(previous)
    
    for each in previous[:length]:
        previous.append(each+[current])
        
    return previous
