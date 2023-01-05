def dailyTemperatures(temp):
        
    stack  = [0]
    length = len(temp)
    output = [0]
        
    for i in range(1, length):
        output.append(0)
        
        while stack and (temp[i] > temp[stack[-1]]):
            output[stack[-1]] = i - stack[-1]
            stack.pop()
            
        stack.append(i)
        
    return output
