# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        resArr = []
        slow,fast = head,head
        while fast and fast.next:
            resArr.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        i = len(resArr) - 1
        while slow:
            resArr[i] += slow.val
            slow = slow.next
            i -= 1
        return max(resArr)
