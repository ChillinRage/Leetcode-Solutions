class MyStack:

    def __init__(self):
        self.myQueue1 = []
        self.myQueue2 = []
        
        self.main = self.myQueue1
        self.spare = self.myQueue2

    def push(self, x: int):
        self.main.append(x)

    def pop(self) -> int:
        while (len(self.main) > 1):
            self.spare.append(self.main.pop(0))
        
        self.main, self.spare = self.spare, self.main
        return self.spare.pop(0)

    def top(self) -> int:
        x = self.pop()
        self.push(x)
        return x

    def empty(self) -> bool:
        return (self.isEmpty1() and self.isEmpty2())
    
    # checks if each queue is empty
    def isEmpty1(self):
        return (not self.myQueue1)
    def isEmpty2(self):
        return (not self.myQueue2)
