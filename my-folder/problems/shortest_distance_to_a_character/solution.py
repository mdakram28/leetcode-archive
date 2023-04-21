class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        last_idx = -float('inf')
        ans = []
        for i in range(len(s)):
            if s[i] == c:
                last_idx = i
            ans.append(i-last_idx)
        
        last_idx = float('inf')
        for i in range(len(s)-1, -1, -1):
            if s[i] == c:
                last_idx = i
            ans[i] = min(last_idx - i, ans[i])
        
        return ans