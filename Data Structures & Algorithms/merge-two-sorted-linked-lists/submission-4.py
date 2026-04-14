# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 == None:
            return list2
        if list2 == None:
            return list1
        head = ListNode()
        cur = head
        l1 = list1
        l2 = list2
        while (l1 and l2):
            if (l1.val >= l2.val):
                cur.next = l2
                l2 = l2.next
            elif (l2.val > l1.val):
                cur.next = l1
                l1 = l1.next
            cur = cur.next
            print(cur.val)
        if (l1):
            cur.next = l1
        else:
            cur.next = l2
        return head.next
            