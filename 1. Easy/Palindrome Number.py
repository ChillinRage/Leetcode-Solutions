def isPalindrome(x):
        x = str(x)
        if len(x) % 2:
            return x[:len(x)//2][::-1] == x[len(x)//2+1:]
        
        return x[:len(x)//2][::-1] == x[len(x)//2:]
