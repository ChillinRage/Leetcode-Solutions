def firstBadVersion(n):
    l = 1
    
    while l < n:
        mid = (l+n)//2
        
        if isBadVersion(mid): # isBadVersion pre-defined
            n = mid
        else:
            l = mid + 1

    return l
