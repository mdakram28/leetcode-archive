class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        totals = [0] * 10001
        for n in nums:
            totals[n] += n
        
        pp = 0
        p = 0
        max_curr = 0
        for i in range(1, 10001):
            curr = max(p, pp+totals[i])
            max_curr = max(max_curr, curr)
            pp = p
            p = curr
        
        return max_curr