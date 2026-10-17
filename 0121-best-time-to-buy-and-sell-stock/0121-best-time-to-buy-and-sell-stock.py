class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        n = len(prices)
        buy = prices[0]
        
        for price in prices[1:]:
            if price < buy:
                buy = price
            profit = price - buy
            max_profit = max(max_profit , profit)

        return max_profit    