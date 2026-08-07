class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(i,newInterval)
                break
        if newInterval not in intervals:
            intervals.append(newInterval)
            i = len(intervals) - 1
        l,r = i,i
        while l > 0 and intervals[l-1][1] >= newInterval[0]:
            l -= 1
        while r < len(intervals) - 1 and intervals[r+1][0] <= newInterval[1]:
            r += 1
        intervals[l] = [min([intervals[l][0],newInterval[0],intervals[r][0]]),max([intervals[r][1],newInterval[1],intervals[l][1]])]
        for _ in range(r-l):
            intervals.pop(l+1)
        return intervals