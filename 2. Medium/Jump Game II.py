def jump(nums):
    last  = len(nums) - 1                     # last index
    track = [2**31 - 1 for i in range(last)]  # set high for every index before last
    track += [0]                              # last index takes 0 leap to reach
    cur   = last - 1
        
    while cur >= 0:
        if nums[cur] == 0:                    # cannot move from pos
            cur -= 1
        elif cur + nums[cur] >= last:         # one leap to end
            track[cur] = 1
            cur -= 1
        else:
            track[cur] = min(track[cur + i] for i in range(1, nums[cur] + 1)) + 1
            cur -= 1
        
    return track[0]
