class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        firstIndex = {}
        ans = -1
        for i, c in enumerate(s):
            if c not in firstIndex:
                firstIndex[c] = i
            else:
                ans = max(ans, i-firstIndex[c]-1)
        
        return ans