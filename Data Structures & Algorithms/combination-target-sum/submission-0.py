class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, cur_path, cur_sum):
            if cur_sum == target:
                res.append(cur_path.copy())
                return 
            if cur_sum > target or index >= len(nums):
                return
            
            cur_path.append(nums[index])
            dfs(index, cur_path, cur_sum + nums[index])
            cur_path.pop()

            dfs(index + 1, cur_path, cur_sum)
        
        dfs(0, [], 0)
        return res