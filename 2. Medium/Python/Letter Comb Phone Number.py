def letterCombinations(digits):
    if len(digits) == 0:
        return []
        
    combis = []
    dic = {'2':'abc','3':'def','4':'ghi','5':'jkl',
           '6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
    
    if len(digits) == 1:
        return list(dic[digits])
        
    for l1 in dic[digits[0]]:
        for c in letterCombinations(digits[1:]):
            combis.append(l1+c)
            
    return combis
