class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cache = {}
        def dfs(i,j):
            if (i,j) in cache:
                return cache[(i,j)]
            if i == len(text1) or j == len(text2):
                cache[(i,j)] = 0
                return cache[(i,j)]
            if text1[i] == text2[j]:
                cache[(i,j)] = 1
                cache[(i,j)] += dfs(i+1,j+1)
                return cache[(i,j)]
            cache[(i,j)] = max(dfs(i+1,j),dfs(i,j+1))
            return cache[(i,j)]
        return dfs(0,0)