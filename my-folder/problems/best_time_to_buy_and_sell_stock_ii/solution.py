class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profits = [0]
        inc_ind = [0]

        for i in range(1,len(prices)):
            num = prices[i]
            while len(inc_ind) > 0 and prices[inc_ind[-1]] >= num:
                inc_ind.pop()
            inc_ind.append(i)
            profits.append(profits[-1])
            buy_ind = max(inc_ind, key=lambda j: prices[i]-prices[j] + profits[j])
            profits[-1] = prices[i] - prices[buy_ind] + profits[buy_ind]
            # print(inc_ind, profits)
        return profits[-1]