def merge(intl):
    i = 0
    intl = sorted(intl, key = lambda x: x[0])
    
    while i < len(intl):
        merged = 0
        
        for _ in range(i+1,len(intl)):
            if intl[i][1] < intl[_][0]:
                break
            if intl[i][0] < intl[_][0] and intl[i][1] > intl[_][1]: #subset
                merged  = 1
                intl[_] = intl[i]
                break
            if intl[i][1] >= intl[_][0] and intl[i][1] <= intl[_][1]: #overlap left
                merged = 1
                intl[_][0] = min(intl[_][0],intl[i][0])
            if intl[i][0] >= intl[_][0] and intl[i][0] <= intl[_][1]: #overlap right
                merged = 1
                intl[_][1] = max(intl[_][1],intl[i][1])
                
            if merged:
                break
                    
        if merged:
            intl.remove(intl[i])
        else:
            i += 1
        
    return intl
