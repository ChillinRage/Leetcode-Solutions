def divide(dividend, divisor):
    if dividend == -2**31 and divisor == -1:
        return 2**31 -1
    
    quot = 0
    sign = (dividend>0) == (divisor>0)
    dividend, divisor = abs(dividend), abs(divisor)
    
    while dividend >= divisor:
        scaled, multi = divisor, 1
        while dividend >= scaled:
            dividend -= scaled
            quot += multi
            multi <<= 1  # bitwise shift (same contextual -
            scaled <<= 1 # - purpose as *= 2)

    if sign:
        return quot
    
    return int('-'+str(quot))
