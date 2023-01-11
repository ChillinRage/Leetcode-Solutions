def reverse(self):
    if x > -10 and x < 10:
        return x
        
    sign = '' if x>0 else '-'
    x = str(abs(x))
        
    last = x[0]
    x = x[:0:-1]

    # check if x out of 32-bit range
    if (int(x) > 214748364) or (int(x)==214748364 and int(last)>7):
        return 0
    
    return int(x + last) * (-1 if sign else 1)
