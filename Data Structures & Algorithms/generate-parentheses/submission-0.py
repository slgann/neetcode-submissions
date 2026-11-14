class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def dfs(left, right, cur_str):
            if len(cur_str) == 2 * n:
                res.append(cur_str)
                return
            if left < n:
                dfs(left+1, right, cur_str + '(')
            if right < left:
                dfs(left, right+1, cur_str + ')')
        
        dfs(0, 0, '')
        return res