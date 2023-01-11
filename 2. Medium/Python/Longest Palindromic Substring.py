def longestPalindrome(s):
        longest = s[0]
        
        for i in range(1,len(s)):
            temp = s[i]      # set s[i] middle of palindrome string
            p, c = i-1, i+1  # left and right pointer
            
            while p >= 0: # add similar char to temp
                if s[p] == s[i]:
                    temp += s[p]
                    p -= 1
                else:
                    break
                
            while c < len(s): # add similar char to temp
                if s[c] == s[i]:
                    temp += s[c]
                    c += 1
                else:
                    break
                
            while p >= 0 and c < len(s): # check left == right
                if s[p] == s[c]:
                    temp = s[p] + temp + s[c]
                    p -= 1 ; c += 1
                else:
                    break
                
            if len(temp) > len(longest):
                longest = temp
                
        return longest
