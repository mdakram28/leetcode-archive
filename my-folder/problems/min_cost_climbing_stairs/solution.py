class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        a = cost[0]
        b = cost[1]
        for step in range(2, len(cost)):
            cost[step] += min(a, b)
            a, b = b, cost[step]
        
        return min(a, b)