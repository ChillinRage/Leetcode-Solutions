def decodeAtIndex(S, K):
    size = 0
    
    for i in S:  # find size of decoded string
        if i.isalpha():
            size += 1
        else:
            size *= int(i)


    for i in S[::-1]: # reverse engineer from the back
        K %= size
        if i.isalpha() and K==0: # letter at found index K
            return i
        
        if i.isalpha(): # reduce index
            size -= 1
        else:
            size //= int(i) # cut size of string by patterns repeated
