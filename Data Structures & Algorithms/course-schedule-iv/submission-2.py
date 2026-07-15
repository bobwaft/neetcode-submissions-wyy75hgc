class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        self.adj = {
            i : [] for i in range(numCourses)
        }

        for course,prereq in prerequisites:
            self.adj[course].append(prereq)

        res = []
        self.cache = {}
        self.visited = set()

        for prereq, target in queries:
            res.append(self.dfs(prereq,target))

        return res

    def dfs(self,node,target):
        if (node,target) in self.cache:
            return self.cache[(node,target)]
        if node == target:
            self.cache[(node,target)] = True
            return True
        self.visited.add(node)
        for n in self.adj[node]:
            if self.dfs(n,target):
                self.cache[(node,target)] = True
                return True
        self.visited.remove(node)
        self.cache[(node,target)] = False
        return False

