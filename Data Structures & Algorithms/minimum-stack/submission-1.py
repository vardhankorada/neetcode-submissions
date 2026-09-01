class MinStack:

    def __init__(self):
        self.stack = []
        self.minUntil = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minUntil) == 0: self.minUntil.append(val)
        elif self.minUntil[-1] > val: self.minUntil.append(val)
        else: self.minUntil.append(self.minUntil[-1])

    def pop(self) -> None:
        self.stack = self.stack[:len(self.stack)-1]
        self.minUntil = self.minUntil[:len(self.minUntil)-1]
        

    def top(self) -> int: return self.stack[-1]
        

    def getMin(self) -> int: return self.minUntil[-1]
        
