class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        res = []
        visited = set()
        rows = len(board)
        cols = len(board[0])
        cache = {}

        trie = Trie()

        for word in words:
            trie.insert(word)

        def dfs(r,c,curr,trie,word):
            if min(r,c) < 0 or r == rows or c == cols or (r,c) in visited or board[r][c] not in curr.children:
                return False
            curr = curr.children[board[r][c]]
            word += board[r][c]
            visited.add((r,c))
            if curr.word and word not in res:
                res.append(word)

            if dfs(r+1,c,curr,trie,word) or dfs(r-1,c,curr,trie,word) or dfs(r,c-1,curr,trie,word) or dfs(r,c+1,curr,trie,word):
                visited.clear()
                return True
            else:
                visited.remove((r,c))
                return False
        
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,trie.root,trie,"")

        return res
