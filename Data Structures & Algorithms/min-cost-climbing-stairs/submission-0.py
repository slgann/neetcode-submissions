class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        d1 = 0
        d2 = 0
        for i in range(2, len(cost)+1):
            curr = min(d1 + cost[i-1], d2 + cost[i-2])
            d2 = d1
            d1 = curr
        return d1