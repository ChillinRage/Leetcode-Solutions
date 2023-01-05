def isValid(s):
    stack = []
    bracks = {'(':')','{':'}','[':']'}
    for br in s:
        if br in ')}]':
            if not len(stack):
                return 0
            if bracks[stack[-1]] != br:
                return 0
            stack.pop(-1)
        else:
            stack.append(br)
            
    if len(stack):
        return 0
    
    return 1
