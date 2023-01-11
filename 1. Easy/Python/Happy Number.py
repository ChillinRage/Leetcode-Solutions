def isHappy(n):
    check = set()
    
    while n > 1 and n not in check:
        check.add(n)
        n = sum(map(int, [int(i)**2 for i in str(n)]))

    return n==1
