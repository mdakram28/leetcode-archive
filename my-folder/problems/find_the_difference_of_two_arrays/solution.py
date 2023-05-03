class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        a1 = [n for n in nums1 if n not in nums2]
        a2 = [n for n in nums2 if n not in nums1]
        return a1, a2