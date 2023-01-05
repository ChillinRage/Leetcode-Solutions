def isNumber(s):
    if '.' in s: #decimal
        pattern1 = '^[+-]{,1}[0-9]+[.]$'
        pattern2 = '^[+-]{,1}[0-9]+[.][0-9]+$'
        pattern3 = '^[+-]{,1}[.][0-9]+$'
        
        if re.search('[eE]',s):
            check = re.search('[eE][-+]{,1}[0-9]+$',s)
            if not check: return
            s = s[:check.span()[0]]
        patterns = [pattern1,pattern2,pattern3]
        return any([re.match(i,s) for i in patterns])
            
    else: #integer
        if 'e' in s or 'E' in s:
            pattern1 = '^[+-]{,1}[0-9]+[eE][+-]{,1}[0-9]+$'
            return re.match(pattern1,s)
        pattern = '^[+-]{,1}[0-9]+$'
        return re.match(pattern,s)
