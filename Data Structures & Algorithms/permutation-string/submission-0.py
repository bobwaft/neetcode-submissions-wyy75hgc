class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Map = {}
        for c in s1:
            if c not in s1Map:
                s1Map[c] = 0
            s1Map[c] += 1
        l = 0
        curMap = {}
        for r in range(len(s2)):
            if (r-l) < len(s1):
                if s2[r] not in curMap:
                    curMap[s2[r]] = 0
                curMap[s2[r]] += 1
            else:
                if s2[r] not in curMap:
                    curMap[s2[r]] = 0
                curMap[s2[r]] += 1
                curMap[s2[l]] -= 1
                l += 1
            res = True
            for c in s1Map:
                res = res and (c in curMap and s1Map[c] == curMap[c])
            if res:
                return True
        return False
