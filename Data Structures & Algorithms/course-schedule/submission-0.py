class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {}
        for pair in prerequisites:
            if pair[0] not in adjList:
                adjList[pair[0]] = []
            adjList[pair[0]].append(pair[1])

        banned = set()

        def dfs(node):
            if node in banned:
                return False
            if node not in adjList:
                return True
            banned.add(node)
            for neighbor in adjList[node]:
                if not dfs(neighbor):
                    return False
            banned.remove(node)
            adjList[node] = []
            return True
        for i,_ in prerequisites:
            if not dfs(i):
                return False
        return True