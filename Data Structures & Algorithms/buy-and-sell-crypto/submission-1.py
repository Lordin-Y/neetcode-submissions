class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best = 0
        price =0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                
                price = prices[j] - prices[i]
                
                best = max(best, price)
        return best