def fib(n):
    pre = 0
    cur = 1
        
    while n > 0:
        pre, cur = cur, (pre + cur)
        n -= 1
        
    return pre
