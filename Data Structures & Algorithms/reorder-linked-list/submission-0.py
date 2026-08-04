# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast,slow = head,head
        first_half_head = head 
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        tmp = slow.next
        slow.next = None
        second_half_head = self.reverseList(tmp)
        head = first_half_head
        while first_half_head and second_half_head:
            first_tmp = first_half_head.next
            second_tmp = second_half_head.next
            first_half_head.next = second_half_head
            second_half_head.next = first_tmp
            first_half_head = first_tmp
            second_half_head = second_tmp


        
        
    def reverseList(self,head):
        if not head:
            return None
        res = head
        if head.next:
            res = self.reverseList(head.next)
            head.next.next = head
        head.next = None
        return res