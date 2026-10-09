# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base Case：如果節點是空的，直接回傳 None
        if not root:
            return None
        
        # 翻轉當前節點的左右子節點
        root.left, root.right = root.right, root.left
        
        # 遞迴向下翻轉子樹
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        # 回傳翻轉後的根節點
        return root
