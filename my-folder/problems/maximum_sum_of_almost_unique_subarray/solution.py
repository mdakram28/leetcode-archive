class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        total = sum(nums[:k])
        
        f = defaultdict(int)
        for num in nums[:k]:
            f[num] += 1
        ans = total if len(f) >= m else 0
        
        for i in range(k, len(nums)):
            f[nums[i]] += 1
            f[nums[i-k]] -= 1
            total += nums[i] - nums[i-k]
            if f[nums[i-k]] == 0:
                del f[nums[i-k]]
            
            if len(f) >= m:
                ans = max(ans, total)
        
        return ans
        