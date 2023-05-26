class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        
        TOTAL = sum(nums)
        total = 0
        max_total = -float('inf')
        max_circ = -float('inf')
        max_non_circ = -float('inf')
        min_total = 0

        for num in nums:
            total += num
            max_total = max(max_total, total)
            max_circ = max(max_circ, max_total + TOTAL-total)

            max_non_circ = max(max_non_circ, total-min_total)
            min_total = min(min_total, total)

        return max(max_circ, max_non_circ)
        