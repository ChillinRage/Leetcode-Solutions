def numberOfBeams(bank):
    if len(bank) == 1:
        return 0
        
    output  = 0
    current = 0
    
    while current < len(bank)-1:
        if '1' not in bank[current]:
            current += 1 
            continue

        for after in range(current+1, len(bank)):
            if '1' in bank[after]:
                break
            
        if '1' not in bank[after]:
            break
                
        output  += bank[current].count('1') * bank[after].count('1')
        current += 1
        
    return output
