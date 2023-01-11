def climbStairs(n):
    if n < 3:
        return n
    
    p, c = 1, 2
    
    for i in range(n-2):
        p, c = c, p + c
        
    return c
