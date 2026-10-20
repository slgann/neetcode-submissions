class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        l = 0
        min_s = nums[k-1] - nums[0]
        
        for r in range(k-1, len(nums)):
            
            score = nums[r] - nums[l]
            min_s = min(min_s, score)
            l += 1
        return min_s