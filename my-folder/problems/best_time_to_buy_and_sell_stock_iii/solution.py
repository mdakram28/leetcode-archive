class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profits = [0] * n
        profit_if_buy = [-prices[0]] * n
        
        for i in range(1, n):
            profit_if_buy[i] = max(
                profit_if_buy[i-1],
                profits[i] - prices[i]
            )
            profits[i] = max(
                profits[i-1],
                profit_if_buy[i] + prices[i]
            )
        

        for i in range(1, n):
            profit_if_buy[i] = max(
                profit_if_buy[i-1],
                profits[i] - prices[i]
            )
            profits[i] = max(
                profits[i-1],
                profit_if_buy[i] + prices[i]
            )
        
        return profits[-1]