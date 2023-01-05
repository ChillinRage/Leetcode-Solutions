def sortColors(nums):
    count = [0,0,0]
    
    for i in nums:
        count[i] += 1
        
    nums[:] = [0 for i in range(count[0])] + [1 for i in range(count[1])] + \
              [2 for i in range(count[2])]
