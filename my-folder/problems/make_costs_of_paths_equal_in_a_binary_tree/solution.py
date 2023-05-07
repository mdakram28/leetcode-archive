class Solution:
    def minIncrements(self, n: int, cost: List[int]) -> int:
        ans = 0
        def dfs(at):
            nonlocal ans
            left = 2*at+1
            right = left+1
            if left >= n: return cost[at]
            
            left_val = dfs(left)
            right_val = dfs(right)
            
            ans += abs(left_val-right_val)
            # cost[left] = cost[right] = max(cost[left], cost[right])
            return max(left_val, right_val) + cost[at]
        
        dfs(0)
        return ans