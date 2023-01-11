def numTrees(n):
    if n <= 1:
        return 1
    else:
        
        left  = 0
        right = n - 1
        ways  = 0
        
        while left <= right:
            if left == right:
                ways += (numTrees(left) ** 2)
            else:
                ways += numTrees(left) * numTrees(right) * 2
                
            left  += 1
            right -= 1
            
        return ways
