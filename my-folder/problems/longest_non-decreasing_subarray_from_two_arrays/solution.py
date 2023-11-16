class Solution:
    def maxNonDecreasingLength(self, nums1: List[int], nums2: List[int]) -> int:
        a = 0
        b = 0
        ac = 0
        bc = 0
        ans = 0
        for n1, n2 in zip(nums1, nums2):
            n1, n2 = max(n1, n2), min(n1, n2)
            n1c = ac+1 if a <= n1 else bc+1 if b <= n1 else 1
            n2c = ac+1 if a <= n2 else bc+1 if b <= n2 else 1
            a, ac = n1, n1c
            b, bc = n2, n2c
            
            ans = max(ans, ac, bc)
        return ans
            