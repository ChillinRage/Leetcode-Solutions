def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    length = len(nums)
    if length == 1 or k == 0:
        return
        
    i = k % length
    val = nums[0]
    repeat = False
    start  = 0
    for _ in range(length):
        val, nums[i] = nums[i], val
        if repeat:
            repeat = False
            start += 1
            i = (start + k) % length
            val = nums[start]
        else:
            i = (i + k) % length
            if i == start:
                repeat = True
