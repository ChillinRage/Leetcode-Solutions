def singleNumber(nums):
    repeat = []
    
    for n in nums:
        if n not in repeat:
            repeat.append(n)
        else:
            repeat.remove(n)

    return repeat[0]
