class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lowest = float('inf')
        for i in range(len(prices)):
            lowest = min(lowest, prices[i])
            profit = max(profit, prices[i] - lowest)
        return profit

