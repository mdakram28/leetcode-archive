class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        end = 0
        total = 0

        min_length = float('inf')
        for start in range(n):
            while end < n and total < target:
                total += nums[end]
                end += 1
            
            if total >= target:
                min_length = min(min_length, end-start)
            
            total -= nums[start]
        
        return min_length if min_length != float('inf') else 0