def isUgly(self, n: int) -> bool:
        if not n:
            return 0
        
        while not n%2:
            n = n//2
        while not n%3:
            n = n//3
        while not n%5:
            n = n//5
            
        return n == 1
