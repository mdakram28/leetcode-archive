class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int], k: int) -> int:
        if k == 0:
            return 0 if nums1 == nums2 else -1
        op_take = 0
        op_put = 0
        for n1, n2 in zip(nums1, nums2):
            if (n1-n2) % k: return -1
            if n1 > n2:
                op_take += (n1-n2)
            else:
                op_put += (n2-n1)
        if op_take != op_put: return -1
        return op_take//k