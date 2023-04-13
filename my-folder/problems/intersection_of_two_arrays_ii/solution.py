class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ret = []
        f = collections.defaultdict(int)
        for n in nums1:
            f[n] += 1
        
        for n in nums2:
            if f[n]:
                ret.append(n)
                f[n] -= 1
        
        return ret