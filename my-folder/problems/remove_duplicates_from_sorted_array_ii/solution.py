class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        freq = {}
        for j in range(len(nums)):
            if freq.get(nums[j], 0) < 2:
                freq[nums[j]] = freq.get(nums[j], 0) + 1
                nums[i] = nums[j]
                i += 1
        
        return i