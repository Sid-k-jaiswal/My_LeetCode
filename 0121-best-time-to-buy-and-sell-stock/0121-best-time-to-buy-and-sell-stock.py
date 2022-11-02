class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if len(prices) < 2:
            return 0

        buy = prices[0]
        profit = 0
        
        for sell in range(1,len(prices)):
            if prices[sell] > buy:
                if profit < prices[sell]-buy:
                    profit = prices[sell]-buy
            else:
                if buy > prices[sell]:
                    buy = prices[sell]
        
        return profit
        