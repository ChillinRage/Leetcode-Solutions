def longestCommonPrefix(strs):
    prefix = ''
    
    for s in strs[0]:
        prefix += s
        for st in strs:
            if prefix != st[:len(prefix)]:
                return prefix[:-1]
            
    return prefix
