class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s1 = set(nums1)
        s2 = set(nums2)
        
        return [
            sum(1 for i, n in enumerate(nums1) if n in s2),
            sum(1 for i, n in enumerate(nums2) if n in s1),
        ]
