# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = [[]]
        if not root:
            return []
        queue = deque()
        queue.append(root)
        height = 0
        while (len(queue)>0):
            for i in range(len(queue)):
                node = queue.popleft()
                res[height].append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append([])
            height += 1
        return res[0:-1]