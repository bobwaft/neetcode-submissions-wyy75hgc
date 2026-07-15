class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {
            i : [] for i in range(numCourses)
        }

        for course,prereq in prerequisites:
            adj[course].append(prereq)

        res = []

        visited = set()
        path = set()
        for i in range(numCourses):
            if not self.dfs(i,res,visited,path,adj):
                return []
        return res

    def dfs(self,node,res,visited,path,adj):
        if node in path:
            return False
        if node in visited:
            return True
        visited.add(node)
        path.add(node)
        for n in adj[node]:
            if not self.dfs(n,res,visited,path,adj):
                return False
        path.remove(node)
        res.append(node)
        return True