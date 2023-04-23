class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        if 1 in nums:
            return n - nums.count(1)
        
        min_dist = float('inf')
        for i in range(n):
            g = nums[i]
            for j in range(i+1, n):
                g = math.gcd(g, nums[j])
                if g == 1:
                    min_dist = min(min_dist, j-i)
        
        if min_dist == float('inf'): return -1
        return min_dist + n-1