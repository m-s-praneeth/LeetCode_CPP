import sys
class MinStack:
    def __init__(self):
        self.stack = []
        self.min = sys.maxsize        
    def push(self, x: int) -> None:
        self.min = min(self.min,x)
        self.stack.append([x,self.min])        
    def pop(self) -> None:
        self.stack.pop()
        if(self.stack):
            self.min = self.stack[-1][1]
        else:
            self.min = sys.maxsize
    def top(self) -> int:
        return self.stack[-1][0]
    def getMin(self) -> int:
        return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()