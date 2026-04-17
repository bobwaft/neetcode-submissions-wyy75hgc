# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isBalanced = True
        def dfs(node):
            if not node:
                return 0
            heightL = dfs(node.left)
            heightR = dfs(node.right)
            if (abs(heightL-heightR) > 1):
                self.isBalanced = False
            print(self.isBalanced)
            return max(heightL,heightR)+1
        dfs(root)
        return self.isBalanced
