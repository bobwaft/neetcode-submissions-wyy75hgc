class MinStack:
    def __init__(self):
        self.stk = []
        self.minList = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        self.minList.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minList.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return sorted(self.minList)[0]
