class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.helper(1,n,k,[],res)
        return res

    def helper(self,i,n,k,cur,res):
        if len(cur) == k:
            res.append(cur.copy())
            return
        if i > n:
            return
        
        for j in range(i,n+1):
            cur.append(j)
            self.helper(j+1,n,k,cur,res)
            cur.pop()