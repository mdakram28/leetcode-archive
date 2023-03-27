class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        curr_min = prices[0]
        max_profit = 0
        for p in prices:
            curr_min = min(curr_min, p)
            max_profit = max(max_profit, p-curr_min)
        return max_profit
