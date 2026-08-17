class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            minVal = min(self.minStack[-1], val)
            self.minStack.append(minVal)
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
           self.stack.pop()
        if self.minStack:
           self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]    

    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
