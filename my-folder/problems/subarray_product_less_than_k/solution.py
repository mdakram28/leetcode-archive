class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        start = 0
        end = 0
        prod = 1
        count = 0
        n = len(nums)
        
        while start < n:
            while end < n and (prod * nums[end]) < k:
                prod *= nums[end]
                end += 1
            
            # print(start, end, prod)
            if end>start:
                count += end-start
                prod //= nums[start]
                start += 1
            elif end == start:
                start += 1
                end += 1

        # count += end-start
        return count