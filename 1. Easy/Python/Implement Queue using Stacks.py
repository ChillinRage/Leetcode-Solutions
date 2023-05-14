class MyQueue:

    def __init__(self):
        self.main = []
        self.spare = []

    def push(self, x: int) -> None:
        self.main.append(x)

    def pop(self) -> int:
        while (self.main):
            self.spare.append(self.main.pop(-1))
        
        x = self.spare.pop(-1)
        
        while (self.spare):
            self.main.append(self.spare.pop(-1))
            
        return x

    def peek(self) -> int:
        while (self.main):
            self.spare.append(self.main.pop(-1))
        
        x = self.spare[-1] # last index represents top of stack
        
        while (self.spare):
            self.main.append(self.spare.pop(-1))
            
        return x

    def empty(self) -> bool:
        return (not self.main)
