class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [0] * (len(nums1)+1)
        max_len = 0

        for r in range(len(nums2)):

            for c in range(len(nums1)-1, -1, -1):
                if nums1[c] == nums2[r]:
                    dp[c+1] = dp[c] + 1
                    max_len = max(max_len, dp[c+1])
                else:
                    dp[c+1] = 0

        return max_len
