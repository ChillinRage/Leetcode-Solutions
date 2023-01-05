def plusOne(digits):
    cur = -1
    ten = 1
    
    while ten:
        ten = 0
        
        if abs(cur) > len(digits):
            return [1] + digits
        
        digits[cur] += 1
        if digits[cur] == 10:
            ten  = 1
            digits[cur] = 0
            cur -= 1
            
    return digits
