class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp_prev = [i for i in range(len(word1)+1)]
        dp = [0]*(len(word1)+1)

        for l2 in range(1, len(word2)+1):
            dp[0] = l2
            for l1 in range(1, len(word1)+1):
                if word1[l1-1] == word2[l2-1]:
                    dp[l1] = dp_prev[l1-1]
                else:
                    dp[l1] = min(
                        dp_prev[l1],
                        dp[l1-1],
                        dp_prev[l1-1]
                    )+1
            # print(dp)
            dp, dp_prev = dp_prev, dp
        
        return dp_prev[-1]