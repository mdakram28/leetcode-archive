class Solution:
    def countPalindromes(self, s: str) -> int:
        f = defaultdict(int)
        total = 0
        DIGITS = "0123456789"
        mod=10**9+7
        for c in s:
            for dig in DIGITS:
                for dig2 in DIGITS:
                    total += f[c+dig2+dig+dig2]
            for dig in DIGITS:
                for dig2 in DIGITS:
                    f[dig2+c+dig+c] += f[dig2+c+dig]
            for dig in DIGITS:
                for dig2 in DIGITS:
                    f[dig2+dig+c] += f[dig2+dig]
            for dig in DIGITS:
                f[dig+c] += f[dig]
            f[c] += 1
            # print({c:val for c, val in f.items() if val}, total)
            
                    
        return total%mod