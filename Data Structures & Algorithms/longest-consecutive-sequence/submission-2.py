class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        max_len = 1
        curr_len = 1
        for i, a in enumerate(nums):
            if i == 0:
                continue
            if a == nums[i-1] + 1:
                curr_len += 1
            elif a == nums[i-1]:
                continue
            else:
                max_len = max(max_len, curr_len)
                curr_len = 1
        return max(max_len, curr_len)