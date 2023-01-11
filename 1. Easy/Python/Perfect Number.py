def checkPerfectNumber(num):
    summ = 1
    
    for i in range(2, int(num ** 0.5) + 1):
        if (num % i == 0):
            summ += i + (num // i)
        
    return (summ == num) and (num != 1)
