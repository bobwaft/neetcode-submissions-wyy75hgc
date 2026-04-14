# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None
        current = head
        if current == None:
            return current
        nextRef = current.next
        while (nextRef != None):
            current.next = prev
            prev = current
            current = nextRef
            nextRef = current.next
        current.next = prev
        return current