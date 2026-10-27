# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        s = f = head
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        second = s.next
        s.next = None

        prev = None
        curr = second
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        l1 = head
        l2 = prev
        while l1 and l2:
            nxt1 = l1.next
            nxt2 = l2.next

            l1.next = l2
            l2.next= nxt1

            l1 = nxt1
            l2 = nxt2
        