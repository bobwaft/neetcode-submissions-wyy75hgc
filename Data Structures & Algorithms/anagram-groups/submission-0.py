class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedstrs = strs[:]
        for i in range(len(sortedstrs)):
            res = ""
            counts = [0]*26
            for char in sortedstrs[i]:
                counts[ord(char)-97] += 1
            for n in range(len(counts)):
                for _ in range(counts[n]):
                    res += chr(n+97)
            sortedstrs[i] = res
        strsdict = {}
        j = 0
        for i in sortedstrs:
            if i not in strsdict:
                strsdict[i] = j
                j+=1
        res = [[] for i in strsdict]
        for i in range(len(sortedstrs)):
            res[strsdict[sortedstrs[i]]].append(strs[i])
        return res