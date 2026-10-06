class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        l = 0
        max_profit = 0

    
        for r in range(l + 1, len(prices)):
            profit = prices[r] - prices[l]
            max_profit = max(max_profit, profit)
            #move only when you find a new opportunity to buy (aka cheaper)
            if prices[r] < prices[l]:
                l = r
        
        return max_profit