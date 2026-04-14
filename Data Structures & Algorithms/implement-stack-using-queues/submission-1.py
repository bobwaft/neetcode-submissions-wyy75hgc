class MyStack:

    def __init__(self):
        self.queue = []
        self.helper = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        while len(self.queue) > 1:
            self.helper.append(self.queue.pop(0))
        temp = self.queue.pop(0)
        while len(self.helper) > 0:
            self.queue.append(self.helper.pop(0))
        return temp

    def top(self) -> int:
        return self.queue[-1]

    def empty(self) -> bool:
        return len(self.queue) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()