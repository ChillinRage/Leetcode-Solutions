def romanToInt(s):
    dic = {'I':1, 'V':5,'X':10,'L':50,
           'C':100, 'D':500, 'M':1000}
        
    summ = 0
    for i in range(len(s)-1):
        if dic[s[i]] < dic[s[1 + i]]:
            summ -= dic[s[i]]
        else:
            summ += dic[s[i]]
            
    return (summ + dic[s[-1]])
