class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # l = 0
        max_l = min(map(len, strs))
        
        for l in range(max_l):
            c = strs[0][l]
            for s in strs:
                if s[l] != c: return strs[0][:l]
        
        return strs[0][:max_l]