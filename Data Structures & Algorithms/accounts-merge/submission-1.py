class UnionFind:
    def __init__(self,accounts):
        self.par = {}
        self.rank = {}
        self.name = {}
        for account in accounts:
            for i in range(1,len(account)):
                self.par[account[i]] = account[i]
                self.name[account[i]] = account[0]
                self.rank[account[i]] = 0

    def find(self,account):
        p = self.par[account]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p
    
    def union(self,acc1,acc2):
        p1,p2 = self.find(acc1),self.find(acc2)
        if p1 == p2:
            return False
        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p2] > self.rank[p1]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1
        return True
    
    def returnLists(self):
        res = {}
        for email in self.par:
            if self.find(email) not in res:
                res[self.find(email)] = [email]
            else:
                res[self.find(email)].append(email)
        return [res[parent] for parent in res]
    
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        edges = []
        for account in accounts:
            for i in range(1,len(account)-1):
                if i+1 < len(account):
                    edges.append([account[i],account[i+1]])
        uf = UnionFind(accounts)
        for edge in edges:
            uf.union(edge[0],edge[1])
        groupedLists = uf.returnLists()
        res = []
        for accounts in groupedLists:
            accounts.sort()
            tmp = [uf.name[accounts[0]]]
            res.append(tmp + accounts)
        return res

        
        
                