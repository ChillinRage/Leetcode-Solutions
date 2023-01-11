def getRow(rowIndex):
    current = [1]
    
    for n in range(1, rowIndex + 1):
        pre  = 0
        cur  = 1
        temp = []
        
        while cur < n:
            temp.append(current[pre] + current[cur])
            pre  = cur
            cur += 1
            
        current = [1] + temp + [1]

    return current
