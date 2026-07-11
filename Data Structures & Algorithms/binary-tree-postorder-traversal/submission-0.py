# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        callstack = [root]
        visitstack = [False]
        while callstack:
            curr,visited = callstack.pop(), visitstack.pop()
            if curr:
                if visited:
                    res.append(curr.val)
                else:
                    callstack.append(curr)
                    visitstack.append(True)
                    callstack.append(curr.right)
                    visitstack.append(False)
                    callstack.append(curr.left)
                    visitstack.append(False)
        return res
        