# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_dia = 0
        def get_depth(node):
            nonlocal max_dia
            if not node:
                return 0
            d_l = get_depth(node.left)
            d_r = get_depth(node.right)
            max_dia = max(max_dia, d_l + d_r)
            return max(d_l, d_r) + 1
        get_depth(root)
        return max_dia 