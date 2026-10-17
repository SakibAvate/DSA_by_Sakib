class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)
        buy = prices[0]

        
        for price in prices[1:]:
            
            buy = min(buy , price)
            max_profit = max(max_profit , price - buy)

        return max_profit    