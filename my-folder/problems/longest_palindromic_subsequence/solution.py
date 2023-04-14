class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        @cache
        def max_subseq(l, r):
            if l == r: return 1
            elif l > r: return 0
            i = r
            if s[l] == s[r]:
                return max_subseq(l+1, r-1)+2
            else:
                return max(max_subseq(l, r-1), max_subseq(l+1, r))
            return ret
        
        return max_subseq(0, len(s)-1)