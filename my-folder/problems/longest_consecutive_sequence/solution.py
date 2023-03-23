class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        idx = {}
        for i, num in enumerate(nums):
            idx[num] = i
        counts = [0] * len(nums)

        def fill(num):
            i = idx[num]
            if counts[i] > 0:
                return counts[i]
            count = 1
            if num+1 in idx:
                count += fill(num+1)
            counts[i] = count
            return count
        
        max_count = 0
        for num in nums:
            max_count = max(max_count, fill(num))
            # print()
    
        return max_count