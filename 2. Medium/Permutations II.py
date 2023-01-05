#Solution 1 (cheese strat)
def permuteUnique1(nums):
    return list(set(i for i in itertools.permutations(nums)))

#Solution 2 (intended approach)
def permuteUnique2(nums):
    output   = []
    main_len = len(nums)
        
    def backtrack(current, counter, length):
        if length == main_len:
            output.append(list(current))
            return
            
        for num in counter:
            if counter[num] > 0:
                current.append(num)
                counter[num] -= 1
                backtrack(current, counter, length + 1)
                    
                current.pop()
                counter[num] += 1
        
    backtrack([], Counter(nums), 0)
        
    return output
