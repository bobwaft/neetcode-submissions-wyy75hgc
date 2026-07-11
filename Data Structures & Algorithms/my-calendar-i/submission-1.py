class TreeNode:
    def __init__(self,start,end):
        self.left = None
        self.right = None
        self.start = start
        self.end = end

class MyCalendar:
    def __init__(self):
        self.root = None

    def insert(self,node,start,end):
        if end <= node.start:
            if not node.left:
                node.left = TreeNode(start,end)
                return True
            return self.insert(node.left,start,end)
        elif start >= node.end:
            if not node.right:
                node.right = TreeNode(start,end)
                return True
            return self.insert(node.right,start,end)
        return False

    def book(self, startTime: int, endTime: int) -> bool:
        if not self.root:
            self.root = TreeNode(startTime,endTime)
            return True
        return self.insert(self.root,startTime,endTime) 
        
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)