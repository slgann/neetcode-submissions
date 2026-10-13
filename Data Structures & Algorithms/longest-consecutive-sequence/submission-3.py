class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        hset = set(nums)
        for n in hset:
            if n-1 not in hset:
                lenght = 1
                while n+lenght in hset:
                    lenght += 1
                res = max(res, lenght)
        return res