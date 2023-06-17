class Solution:
    def minCost(self, nums: List[int], x: int) -> int:
        n = len(nums)
        
        min_cost = [*nums]
        ans = sum(min_cost)
        
        for rot in range(1, len(nums)):
            for i in range(len(nums)):
                min_cost[i] = min(min_cost[i], nums[(i+rot)%n])
            ans = min(ans, sum(min_cost)+rot*x)
        
        return ans
                
                