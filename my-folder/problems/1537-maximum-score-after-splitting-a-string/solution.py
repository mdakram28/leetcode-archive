class Solution:
    def maxScore(self, s: str) -> int:
        
        right = s.count("1")
        left = 0
        ans = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                left += 1
            else:
                right -= 1
            ans = max(ans, left+right)
        
        return ans
