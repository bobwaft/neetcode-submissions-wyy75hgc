class DynamicArray:
    
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n
        if i > self.size:
            self.size += 1

    def pushback(self, n: int) -> None:
        if (self.size == self.capacity):
            self.resize()
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        self.size -=1
        temp = self.arr[self.size]
        self.arr[self.size] = 0        
        return temp 

    def resize(self) -> None:
        self.arr = self.arr + [0]*self.capacity
        self.capacity *= 2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity