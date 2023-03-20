class Solution:
    def jobScheduling(self, startTimes: List[int], endTimes: List[int], profits: List[int]) -> int:
        jobs = list(zip(startTimes, endTimes, profits))
        jobs.sort(key=lambda x: x[1])

        profits = [(0, 0)] # (time, profit)

        def bin_search(target):
            l = 0
            r = len(profits)
            while (r-l) > 1:
                mid = (l+r)//2
                if profits[mid][0] <= target:
                    l = mid
                else:
                    r = mid
            return profits[l][1]

        max_profit = 0

        for startTime, endTime, profit in jobs:
            # print(profit)
            new_profit = bin_search(startTime) + profit
            max_profit = max(max_profit, new_profit)
            if profits[-1][0] == endTime:
                profits.pop()
            profits.append((endTime, max_profit))
        # print(profits)
        return max_profit
