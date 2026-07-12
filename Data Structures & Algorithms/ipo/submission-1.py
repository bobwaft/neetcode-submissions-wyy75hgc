class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        profitsheap = [] #maxheap
        capitalheap = [(c,p) for c,p in zip(capital,profits)] #minheap
        heapq.heapify(capitalheap)
        res = 0
        for _ in range(k):
            while capitalheap and capitalheap[0][0] <= w:
                tmp = heapq.heappop(capitalheap)[1]
                heapq.heappush(profitsheap,-1*tmp)
            if profitsheap:
                w += heapq.heappop(profitsheap)*-1
        return w