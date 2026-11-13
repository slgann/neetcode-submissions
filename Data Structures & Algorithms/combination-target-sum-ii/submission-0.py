class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(index, cur_path, cur_sum):
            if cur_sum == target:
                res.append(cur_path.copy())
                return
            if cur_sum > target or index >= len(candidates):
                return
            cur_path.append(candidates[index])
            dfs(index + 1, cur_path, cur_sum + candidates[index])
            cur_path.pop()
            while index + 1 < len(candidates) and candidates[index] == candidates[index+1]:
                index += 1
            dfs(index + 1, cur_path, cur_sum)
        dfs(0, [], 0)
        return res