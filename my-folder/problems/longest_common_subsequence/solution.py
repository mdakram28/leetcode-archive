class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp_prev = [0] * (len(text1) + 1)
        dp_curr = [0] * (len(text1) + 1)

        for r in range(1, len(text2)+1):
            dp_curr.clear()
            dp_curr.append(0)
            for c in range(1, len(text1)+1):
                if text1[c-1] == text2[r-1]:
                    dp_curr.append(dp_prev[c-1] + 1)
                else:
                    dp_curr.append(max(dp_curr[c-1], dp_prev[c]))
            dp_prev, dp_curr = dp_curr, dp_prev
        
        return dp_prev[-1]