class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        f1 = [False] * 10
        for n in nums1:
            f1[n] = True
        
        min_common = 100
        for n in nums2:
            if f1[n] and n < min_common:
                min_common = n
        if min_common<10:
            return min_common
        
        d1, d2 = min(nums1), min(nums2)
        
        return min(d1, d2)*10 + max(d1, d2)