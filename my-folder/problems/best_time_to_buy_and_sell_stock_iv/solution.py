class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        profits_if_buy = [-prices[0]] * n
        profits = [0] * n

        # for i in range(1, n):
        #     profits_if_buy[i] = max(profits_if_buy[i], profits_if_buy[i-1])

        for trans in range(k):

            for i in range(1, n):
                profits_if_buy[i] = max(
                    profits[i] - prices[i],
                    profits_if_buy[i-1]
                )
                profits[i] = max(
                    profits[i-1],
                    profits_if_buy[i] + prices[i]
                )


        
        return profits[-1]