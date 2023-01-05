def myAtoi(s):
    s = s.lstrip()  # remove leading whitespace
    if s == '':
        return 0
        
    if s[0] == '-' or s[0] == '+':
        status = ('-' if s[0] == '-' else '')
        s      = s[1:]
    else:
        status = ''
        
    integer = '0'
    for char in s:
        if char not in '0123456789':
            break
        else:
            integer += char
        
    integer = int(status + integer)
    
    if integer > 2147483647: # integer out of 32-bit range
        return 2147483647
    elif integer < -2147483648:
        return -2147483648
    else:
        return integer
