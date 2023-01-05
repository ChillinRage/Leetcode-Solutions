def uniquePaths(m, n):
    tot_fact = factorial(m+n-2)
    r_fact   = factorial(n-1)
    nr_fact  = factorial(m+n-2-n+1)
    
    return tot_fact//(r_fact*nr_fact)

def factorial(n):
    num = 1
    
    for i in range(1,n+1):
        num *= i
        
    return num
