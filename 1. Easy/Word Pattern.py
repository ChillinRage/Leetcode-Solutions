def wordPattern(pattern, s):
    s = s.split()
    pairs = {}
    
    if len(s) != len(pattern):
        return 0
    
    for i in range(len(pattern)):
        if pattern[i] not in pairs:
            if s[i] in pairs.values():
                return False
            
            pairs[pattern[i]] = s[i]
        if pairs[pattern[i]] != s[i]:
            return False
        
    return True
