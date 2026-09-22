# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def isSubtree(
        self, root: Optional[TreeNode], subRoot: Optional[TreeNode]
    ) -> bool:
        seen_hashes = set()

        # 1. 專門給大樹用的函式：會加入集合
        def serialize_and_add(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            left = serialize_and_add(node.left)
            right = serialize_and_add(node.right)
            current_str = f"({node.val},{left},{right})"
            seen_hashes.add(current_str)  # 大樹才要紀錄
            return current_str

        # 2. 專門給小樹用的函式：只回傳字串，絕不加入集合
        def serialize_only(node: Optional[TreeNode]) -> str:
            if not node:
                return "#"
            left = serialize_only(node.left)
            right = serialize_only(node.right)
            return f"({node.val},{left},{right})"

        # 執行大樹收集
        serialize_and_add(root)

        # 執行小樹計算（此時不會污染集合了）
        sub_str = serialize_only(subRoot)

        # 最終比對
        return sub_str in seen_hashes
