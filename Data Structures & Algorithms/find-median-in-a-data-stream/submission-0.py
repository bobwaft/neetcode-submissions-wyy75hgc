class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-1*num)
        if self.small and self.large and (self.small[0]*-1 > self.large[0]):
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large,tmp*-1)
        if len(self.small) > len(self.large) + 1:
            tmp = heapq.heappop(self.small)
            heapq.heappush(self.large,tmp * -1)
        elif len(self.large) > len(self.small) + 1:
            tmp = heapq.heappop(self.large)
            heapq.heappush(self.small,tmp * -1)
        print(self.small,self.large)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return self.small[0]*-1
        elif len(self.small) < len(self.large):
            return self.large[0]
        else:
            return (self.large[0]+(self.small[0]*-1))/2