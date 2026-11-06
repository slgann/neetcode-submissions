# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = []
        curr = root
        
        
        while curr or stack:
            
            # 內層迴圈：只要左邊還有路，就一路向左衝到底
            while curr:
                stack.append(curr)    
                curr = curr.left      
            
            
            node = stack.pop()
            
            # 每彈出一個，就代表抓到了一個從小到大排好序的數字
            k -= 1                    
            if k == 0:                
                return node.val       
            
            
            curr = node.right
