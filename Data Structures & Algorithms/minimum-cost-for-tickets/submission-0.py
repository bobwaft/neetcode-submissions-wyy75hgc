class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        cache = {}
        res = self.helper(0,days,costs,cache)
        return res 

    def helper(self,i,days,costs,cache):
        if i in cache:
            return cache[i]
        if i >= len(days):
            return 0
        dayPass = costs[0]+self.helper(i+1,days,costs,cache)
        j = i
        while j < len(days) and days[j] < days[i] + 7:
            j += 1
        weekPass = costs[1]+self.helper(j,days,costs,cache)
        while j < len(days) and days[j] < days[i] + 30:
            j += 1
        monthPass = costs[2]+self.helper(j,days,costs,cache)
        cache[i] = min([dayPass,weekPass,monthPass])
        return cache[i]