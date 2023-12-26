class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @cache
        def num_ways(n, target):
            if target < n: return 0
            if n == 0: return 1 if target == 0 else 0
            return sum(num_ways(n-1, target-i) for i in range(1, k+1))%(10**9+7)
        
        return num_ways(n, target)