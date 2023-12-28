class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        
        # comp = []
        # l = 0
        # for r in range(1, len(s)+1):
        #     if r == len(s) or s[r] != s[r-1]:
        #         comp.append((s[l], r-l))
        #         l = r

        @cache
        def getMinLen(l, k, pchar, pcount):
            
            if l == len(s):
                return 1 + (len(str(pcount)) if pcount > 1 else 0)
            
            # Taking
            if s[l] == pchar:
                ans = getMinLen(l+1, k, s[l], pcount+1)
            else:
                ans = 1 + (len(str(pcount)) if pcount > 1 else 0)
                ans += getMinLen(l+1, k, s[l], 1)
            
            # Skipping
            if k > 0:
                ans = min(ans, getMinLen(l+1, k-1, pchar, pcount))
            
            # print(f"{l=}, {k=}, {pchar=}, {pcount=}, {ans=}")
            
            return ans
        
        return getMinLen(0, k, None, 1)-1