class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.heap = [0]
        self.k = k
        for i in nums:
            self.add(i)
        print(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) - 1 < self.k:
            self.heap.append(val)
            i = len(self.heap) - 1
            while i > 1 and self.heap[i] < self.heap[i//2]:
                temp = self.heap[i]
                self.heap[i] = self.heap[i//2]
                self.heap[i//2] = temp
                i = i//2
        elif self.heap[1] < val:
            self.heap[1] = val
            i = 1
            while 2*i < len(self.heap):
                if (2*i + 1 < len(self.heap) and self.heap[2*i + 1] < self.heap[2*i]
                and self.heap[i] > self.heap[2*i + 1]):
                    temp = self.heap[2*i + 1]
                    self.heap[2*i + 1] = self.heap[i]
                    self.heap[i] = temp
                    i = 2*i + 1
                elif self.heap[i] > self.heap[2*i]:
                    temp = self.heap[2*i]
                    self.heap[2*i] = self.heap[i]
                    self.heap[i] = temp
                    i = 2*i
                else:
                    break
        print(self.heap)
        return self.heap[1]
