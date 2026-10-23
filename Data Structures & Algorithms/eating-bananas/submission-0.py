class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low = 1
        high = max(piles)
        while low <= high:
            mid = (low+high) // 2
            time = 0
            for x in piles:
                time += math.ceil(x/mid)
            if time <= h:
                high = mid - 1
            else:
                low = mid + 1
        return max(low, mid, high)