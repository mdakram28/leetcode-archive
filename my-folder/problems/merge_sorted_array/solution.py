class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return
        mi = 0

        while mi < m:
            if nums1[mi] > nums2[0]:
                num, nums1[mi] = nums1[mi], nums2[0]
                
                ni = 0
                while ni < n-1 and nums2[ni+1] < num:
                    nums2[ni] = nums2[ni+1]
                    ni += 1
                nums2[ni] = num
            mi += 1
        
        nums1[m:] = nums2
