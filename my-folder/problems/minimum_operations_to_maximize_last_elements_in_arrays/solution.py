class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        
        def to_split(a, b):
            ret = 0
            for x, y in zip(nums1[:-1], nums2[:-1]):
                if x <= a and y <= b:
                    continue
                elif x <= b and y <= a:
                    ret += 1
                else:
                    return float('inf')
            return ret
        
        ans = min(
            to_split(nums1[-1], nums2[-1]),
            1 + to_split(nums2[-1], nums1[-1])
        )
        
        return -1 if ans == float('inf') else ans