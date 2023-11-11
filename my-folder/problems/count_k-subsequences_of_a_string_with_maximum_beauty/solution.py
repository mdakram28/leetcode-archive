class Solution:
    def countKSubsequencesWithMaxBeauty(self, s: str, k: int) -> int:
        f = defaultdict(int)
        mod = 10**9+7
        for c in s:
            f[c] += 1
        
        counts = list(f.values())
        counts.sort(reverse=True)
        
        # print(counts)
        ans = counts[:k]
        last = ans[-1]
        ans = ans[:ans.index(last)]
        counts = counts[:counts.index(last)+counts.count(last)]
        
        @cache
        def multiply(i, rem):
            nonlocal total
            if rem == 0:
                return 1
            if i >= len(counts):
                return 0
            
            ret = (counts[i]*multiply(i+1, rem-1))%mod
            if len(counts)-(i+1) >= rem:
                ret = (ret + multiply(i+1, rem))%mod
            return ret
        
        total = multiply(len(ans), k-len(ans))
        for num in ans:
            total = (total*num)%mod
        
        return total
        