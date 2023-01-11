def generateParenthesis(n):
     if n == 1:
        return ['()']
    else:
        previous = generateParenthesis(n - 1)
        
    output = set()
    for each in previous:
        for i in range(2*n + 1):
            output.add(each[:i] + '()' + each[i:])
                
    return list(output)
