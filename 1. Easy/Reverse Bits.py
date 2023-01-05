def reverseBits1(n):
    binary = bin(n)[:1:-1]
    
    if len(binary) < 32:
        binary += '0'*(32-len(binary))
        
    return int(binary,2)

def reverseBits2(n):
    binary = ''
    length = 0
    
    while n > 0:
        binary += str(n%2)
        n //= 2
        length += 1

    if length < 32:
        binary += '0' * (32 - length)
        
    return int(binary, 2)
