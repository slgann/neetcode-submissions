# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_far):
            if not node:
                return 0
            if node.val >= max_far:
                good_count = 1
            else:
                good_count = 0
            
            next_max = max(node.val, max_far)

            left_count = dfs(node.left, next_max)
            right_count = dfs(node.right, next_max)

            return good_count + left_count + right_count

        return dfs(root, root.val)
        