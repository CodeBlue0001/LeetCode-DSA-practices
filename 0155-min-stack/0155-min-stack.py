class MinStack:

    def __init__(self):
        self._stack=[]
        
        self._min=None
        # _hmap={}
    def push(self, value: int) -> None:
        self._stack+=[value]
        if self._min !=None:
            self._min=min(self._min,value)
        else:
            self._min=value

    def pop(self) -> None:
        self._stack.pop()
        if self._stack:
            self._min=min(self._stack)
        else:
            self._min=None
    def top(self) -> int:
        return self._stack[-1]

    def getMin(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()