class Solution:
    def minCut(self, s: str) -> int:
        
        @cache
        def ispal(l, r):
            if r <= l: return True
            if s[l] == s[r]:
                return ispal(l+1, r-1)
            else:
                return False
        
        @cache
        def getmincuts(l):
            if l==len(s):
                return 0
            if ispal(l, len(s)-1):
                return 0
            ans = len(s)-l-1
            for r in range(l, len(s)):
                if ispal(l, r):
                    ans = min(ans, 1+getmincuts(r+1))
            return ans
        
        return getmincuts(0)