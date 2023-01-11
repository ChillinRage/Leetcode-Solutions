def findComplement(num):
    binum = bin(num)[2:]
    comp  = ""
    
    for each in binum:
        if each == "1":
            comp += "0"
        else:
            comp += "1"
            
    return int(comp, 2)
