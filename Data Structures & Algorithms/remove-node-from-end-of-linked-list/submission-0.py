# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        fast,slow = head,head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            length += 2
        if fast:
            length += 1
        i = length
        cur,prev = head, None
        while cur:
            if i == n and prev:
                prev.next = cur.next
                return head
            elif i == n and not prev:
                return cur.next
            prev = cur
            cur = cur.next
            i -= 1
        return head
