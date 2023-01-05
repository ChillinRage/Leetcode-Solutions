def isIsomorphic(s, t):
    pairs = {}
    
    for i in range(len(s)):
        if s[i] not in pairs:
            if t[i] in pairs.values():
                return False
            
            pairs[s[i]] = t[i]
                
        if pairs[s[i]] != t[i]:
            return False

    return True
