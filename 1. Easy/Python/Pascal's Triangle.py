def generate(numRows):
    output = [[1]]
    
    for n in range(2, numRows + 1):
        pre  = 0
        cur  = 1
        row  = output[n - 2]
        temp = []
        
        while cur < n - 1:
            temp.append(row[pre] + row[cur])
            pre  = cur
            cur += 1
            
        output.append([1] + temp + [1])
        
    return output
