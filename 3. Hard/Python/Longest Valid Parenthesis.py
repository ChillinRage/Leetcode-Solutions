def longestValidParentheses(s):
    longest = 0
    length  = 0
    stack   = []
    max_len = len(s)
        
    for i in range(max_len):
        if s[i] == '(':
            stack.append(i)
        elif not stack:
            return max(longest, length, longestValidParentheses(s[i+1:]))
        else:
            stack.pop()
            
        length += 1
            
    if stack:
        stack.append(max_len)
        return largest_diff([-1] + stack)
                
    return max(longest, length)
    
def largest_diff(nums):
    maxm = 0
    
    for i in range(1, len(nums)):
        prev = nums[i - 1]
        cur  = nums[i]
        maxm = max(maxm, cur - prev - 1)
        
    return maxm
