class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        for num in nums:
            num.sort()
        
        m = len(nums)
        n = max(map(len, nums))
        
        total = 0
        for c in range(n):
            max_val = 0
            for r in range(m):
                if c < len(nums[r]) and nums[r][c] > max_val:
                    max_val = nums[r][c]
            total += max_val
        return total