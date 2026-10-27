# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next: # head長度等於0或1
            return True
        
        slow = fast = head 
        while fast.next and fast.next.next: # 切斷串列
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None

        prev = None 
        curr = second
        while curr: # 反轉
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        p1 = head
        while prev is not None:
            if p1.val != prev.val:
                return False
            p1 = p1.next
            prev = prev.next
        return True
        

