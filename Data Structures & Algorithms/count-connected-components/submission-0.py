class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = {}
        rank = {}
        res = 0
        seen = set()
        for i in range(n):
            par[i] = i
            rank[i] = 0

        def find(node):
            p = par[node ]
            while p != par[p]:
                par[p] = par[par[p]]
                p = par[p]
            return p
        
        def union(n1,n2):
            n1,n2 = find(n1),find(n2)
            if n1 == n2:
                return False
            if rank[n1] > rank[n2]:
                par[n2] = n1
            elif rank[n2] > rank[n1]:
                par[n1] = n2
            else:
                par[n1] = n2
                rank[n2] += 1
        
        for (n1,n2) in edges:
            union(n1,n2)
        
        for node in range(n):
            if find(node) not in seen:
                res += 1
                seen.add(find(node))
        
        return res