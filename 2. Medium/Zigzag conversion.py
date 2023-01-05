def convert(s, R):
    # this is very math heavy and I only found
    # the formula after observing the pattern.
    
    if R == 1:
        return s
    
    scale = [(R-1)*2,0]
    output = ''
    
    for i in range(R): # iterate by row
        temp = i
        pointer = 0
        
        while temp < len(s):
            output += s[temp]
            temp += scale[pointer]
                
            if scale[1] and (pointer == 0):
                pointer = 1
            elif pointer == 1:
                pointer = 0
                
        scale[0] -= 2
        scale[1] += 2
        if scale[0] == 0:
            scale = scale[::-1]
            
    return output
