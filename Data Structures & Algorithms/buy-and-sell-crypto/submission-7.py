class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        lowestPrice = prices[0]
        maxprofit = 0
        for i in range(size):
            if prices[i] < lowestPrice:
                lowestPrice = prices[i]
            profit = prices[i] - lowestPrice
            maxprofit = max(profit, maxprofit)
        return maxprofit if maxprofit > 0 else 0


        
