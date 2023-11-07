class Solution:
    def lengthOfLongestSubsequence(self, nums: List[int], target: int) -> int:
        
        # DP[t] : longest seq to make t
        DP = [0] + [-float('inf')] * (target+1)
        for num in nums:
            # print(DP)
            for t in range(target, -1, -1):
                DP[t] = max(
                    DP[t-num] + 1 if t-num >= 0 else -float('inf'),
                    DP[t]
                )
        # print(DP)
        
        
#         def getLength(i, t):
#             if t == 0:
#                 return 0
#             if i <= -1 or t < 0:
#                 return -float('inf')
            
#             return max(
#                 getLength(i-1, t-nums[i]) + 1,
#                 getLength(i-1, t)
#             )
        
        ans = DP[target]
        return -1 if ans == -float('inf') else ans