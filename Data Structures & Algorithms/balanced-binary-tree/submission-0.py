# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return (True, 0)
            
            left_b, left_h = dfs(node.left)
            right_b, right_h = dfs(node.right)

            curr_b = (
                left_b and
                right_b and
                abs(left_h - right_h) <= 1
            )
            curr_h = max(left_h, right_h) + 1
            return (curr_b, curr_h)
        is_tree_balanced, _ = dfs(root)
        return is_tree_balanced
        dfs(root)