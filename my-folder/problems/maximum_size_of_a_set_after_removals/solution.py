class Solution:
    def maximumSetSize(self, nums1: List[int], nums2: List[int]) -> int:
        # taken = set()
        n = len(nums1)
        nums1 = set(nums1)
        nums2 = set(nums2)
        
        common = nums1 & nums2
        for num in common:
            if len(nums1) > len(nums2):
                nums1.remove(num)
            else:
                nums2.remove(num)
        
        
        
        
        return min(len(nums1), n//2) + min(len(nums2), n//2)
        