class Solution:
    def minWindow(self, s: str, t: str) -> str:
        windowCount = dict.fromkeys(t,0)
        tCount = dict.fromkeys(t,0)
        for c in t:
            tCount[c] += 1
        l = 0
        while l < len(s) and s[l] not in windowCount:
            l += 1
        best = ""
        for r in range(l,len(s)):
            if s[r] in windowCount:
                windowCount[s[r]] += 1
            res = True
            for c in windowCount:
                if windowCount[c] > tCount[c]:
                    while s[l] not in windowCount or windowCount[s[l]] > tCount[s[l]]:
                        if s[l] in windowCount and windowCount[s[l]] > tCount[s[l]]:
                            windowCount[s[l]] -= 1
                        l += 1
                res = res and windowCount[c] >= tCount[c]
            print(s[l:r+1])
            if res and ((r-l+1) < len(best) or best == ""):
                best = s[l:r+1]
        return best
            