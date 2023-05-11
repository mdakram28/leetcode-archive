class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n1 = len(nums1)
        n2 = len(nums2)
        dp_prev = [0] * (n1+1)
        dp = [0] * (n1+1)

        for j in range(n2):
            # dp_next
            for i in range(n1):
                dp[i] = max(
                    dp[i-1], 
                    dp_prev[i], 
                    dp_prev[i-1] + 1 if nums1[i] == nums2[j] else 0)
            dp, dp_prev = dp_prev, dp
            # print(j, dp)
        
        return dp_prev[-2]