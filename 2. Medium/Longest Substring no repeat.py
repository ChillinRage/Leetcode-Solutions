def lengthOfLongestSubstring(string):
    if len(string) <= 1: return len(string)
        
    longest = 1
    temp = string[0]
    
    for s in string[1:]:
        if s in temp:
            if len(temp) > longest:
                longest = len(temp)
            temp = temp[temp.index(s)+1:]
            
        temp += s
        
    if len(temp) > longest:
        longest = len(temp)
        
    return longest
