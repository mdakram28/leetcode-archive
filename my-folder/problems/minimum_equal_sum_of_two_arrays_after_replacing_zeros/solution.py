class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        z1 = nums1.count(0)
        z2 = nums2.count(0)
        
        m1 = sum(nums1) + z1
        m2 = sum(nums2) + z2
        
        if z1 == 0 and z2 == 0:
            return m1 if m1 == m2 else -1
        elif z1 == 0:
            return m1 if m2 <= m1 else -1
        elif z2 == 0:
            return m2 if m1 <= m2 else -1
        else:
            return max(m1, m2)