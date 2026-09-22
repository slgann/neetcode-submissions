# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        seen = set()

        def serialize(node: Optional[TreeNode], add_to_set:False) -> str:
            if not node:
                return "#"
            left_str = serialize(node.left, add_to_set)
            right_str = serialize(node.right, add_to_set)
            curr_str = f"({node.val}, {left_str}, {right_str})"
            if add_to_set:
                seen.add(curr_str)
            return curr_str
        
        serialize(root, add_to_set = True)
        sub_str = serialize(subRoot, add_to_set = False)
        return sub_str in seen
        