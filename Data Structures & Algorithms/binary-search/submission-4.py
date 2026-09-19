class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        while l <= h:
            mid = (l+h) // 2
            guess = nums[mid]
            if target not in nums:
                return -1
            elif guess == target:
                return mid
            elif guess > target:
                h = mid - 1
            else:
                l = mid + 1
        