class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float("inf")
        best_price = 0
        for i in range(len(prices)):
            min_price = min(min_price,prices[i])
            best_price = max(best_price, (prices[i] - min_price))
        return best_price