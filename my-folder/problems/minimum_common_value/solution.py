class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i, j = 0, 0
        n1, n2 = len(nums1), len(nums2)
        while i < n1 and j < n2:
            while i<n1 and nums1[i] < nums2[j]:
                i += 1
            if i == n1:
                return -1
            while j<n2 and nums2[j] < nums1[i]:
                j += 1
            if j == n2:
                return -1
            
            if nums1[i] == nums2[j]:
                return nums1[i]
            
        return -1
                