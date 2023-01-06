@cache # available in py 3.9+
def isScramble(s1: str, s2: str):
    length1 = len(s1)
    length2 = len(s2)
        
    if length1 == 1:
        return s1 == s2
    elif (length1 != length2) or (sorted(s1) != sorted(s2)):
        return False
    else:
        for i in range(1, length1):
            if ((isScramble(s1[:i], s2[:i]) and isScramble(s1[i:], s2[i:]))
                or (isScramble(s1[:i], s2[-i:]) and isScramble(s1[i:], s2[:-i]))):
                return True
            
        return False
