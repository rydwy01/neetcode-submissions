class MinStack:

    def __init__(self):
        self.prevMinIdxs = []
        self.stack = []
        # self.prevMinIdx = 0
        self.curMinIdx = -1

    def push(self, val: int) -> None:
        #If first one, append and set curMinIdx to 0, otherwise compare to prev min
        self.stack.append(val)
        if len(self.stack) > 1:
            if self.stack[-1] < self.stack[self.curMinIdx]:
                self.prevMinIdxs.append(self.curMinIdx)
                self.curMinIdx = len(self.stack) - 1
        else:
            self.curMinIdx = 0


        

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack:
            self.curMinIdx = -1
            if self.prevMinIdxs:
                self.prevMinIdxs.pop()
        # print(self.curMinIdx)
        # print(len(self.stack))
        elif self.curMinIdx == len(self.stack):
            self.curMinIdx = self.prevMinIdxs[-1]
            self.prevMinIdxs.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack[self.curMinIdx]
        
