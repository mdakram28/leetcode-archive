class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        freq_mask = 1<<20
        num_mask = ~freq_mask
        
        ret = []
        for i in range(len(nums)):
            n = nums[i]&num_mask
            if nums[n-1]&freq_mask:
                ret.append(n)
            else:
                nums[n-1] |= freq_mask
        return ret