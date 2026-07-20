class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = []
        res = []
        l = 0
        for r in range(len(nums)):
            if r-l+1 < k:
                heapq.heappush(window,(-nums[r],r))
            else:
                heapq.heappush(window,(-nums[r],r))
                while l > window[0][1] or window[0][1] > r:
                    heapq.heappop(window) 
                res.append(-window[0][0])
                l+=1
        return res