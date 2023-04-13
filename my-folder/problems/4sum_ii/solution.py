class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n = len(nums1)
        count = collections.defaultdict(int)
        
        for i in nums1:
            for j in nums2:
                count[i+j] += 1
        
        total = 0
        for k in nums3:
            for l in nums4:
                total += count[-(k + l)]
        
        return total