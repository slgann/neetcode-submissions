# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        dia = []  # 儲存每條路線（每個節點作為轉折點）的直徑長度
    
    # 輔助函式：用來計算某個節點向下的最大深度
        def get_depth(node):
            if not node:
                return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

    # 使用 Stack 進行 DFS 走訪每一個節點
        stack = [root]
    
        while stack:
            curr = stack.pop()  # 取出當前節點
        
        # 1. 計算當前節點的左、右子樹最大深度
            d_l = get_depth(curr.left)
            d_r = get_depth(curr.right)
        
        # 2. 將這條路線的長度（左 + 右）更新到 dia 陣列中
            dia.append(d_l + d_r)
        
        # 3. 繼續將子節點推入 stack，確保每條路線都會被尋訪
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)

    # 4. 從所有路線長度中，選出最長的直徑
        return max(dia)
