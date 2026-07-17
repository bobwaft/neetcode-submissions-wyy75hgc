class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        cache = {}
        return self.dfs(0,m,n,strs,cache)
    def dfs(self,i,m,n,strs,cache):
        if i == len(strs):
            return 0
        if (i,m,n) in cache:
           return cache[(i,m,n)] 
        cache[(i,m,n)] = self.dfs(i+1,m,n,strs,cache)
        ones,zeroes = self.count10(strs[i])
        if m - zeroes >=0 and n - ones >= 0:
            include  = self.dfs(i+1,m-zeroes,n-ones,strs,cache) + 1
            cache[(i,m,n)] = max(cache[(i,m,n)],include)
        return cache[(i,m,n)]

    def count10(self,string):
        ones, zeroes = 0,0
        for c in string:
            if c == "1":
                ones += 1
            if c == "0":
                zeroes += 1
        return (ones,zeroes)