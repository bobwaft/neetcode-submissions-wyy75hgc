# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        #Iterative

        # res = []
        # callstack = []
        # curr = root
        # while curr or callstack:
        #     if curr:
        #         res.append(curr.val)
        #         if curr.right:
        #             callstack.append(curr.right)
        #         curr = curr.left
        #     else:
        #         curr = callstack.pop()
        # return res

        #Recursive

        res = []

        def preorder(node):
            if node:
                res.append(node.val)
                preorder(node.left)
                preorder(node.right)

        preorder(root)
        return res