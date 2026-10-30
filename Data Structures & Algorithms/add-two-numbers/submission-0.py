# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        curr =dummy
        count = 0
        p1 = l1
        p2 = l2
        while p1 or p2 or count:
            val1 = p1.val if p1 else 0
            val2 = p2.val if p2 else 0
            total = val1 + val2 + count
            count = total // 10
            num = total % 10
            curr.next = ListNode(num)
            curr = curr.next
            if p1: p1 = p1.next
            if p2: p2 = p2.next
        return dummy.next