class Solution:
    def minimumBeautifulSubstrings(self, s: str) -> int:
        powers = {1, 5, 25, 125, 625, 3125, 15625, 78125, 390625, 1953125}

        @cache
        def partition(l):
            if l == len(s): return 0
            if s[l] == '0': return float('inf')
            
            ans = float('inf')
            num = 0
            for r in range(l, len(s)):
                num = (num<<1)
                if s[r] == '1':
                    num |= 1
                if num in powers:
                    ans = min(ans, 1+partition(r+1))
            
            return ans
        
        ans = partition(0)
        if ans == float('inf'):
            return -1
        return ans