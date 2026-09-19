class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        maxp = 0
        while j < len(prices):
            if prices[i] < prices[j]:
                profit = prices[j] - prices[i]
                maxp = max(maxp, profit)
            else:
                i = j
            j = j + 1
        return maxp