class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        n = len(s)
        max_dig = len(str(k))
        @cache
        def num_parts(i):
            if i == n:
                return 0
            
            num = 0
            min_parts = float('inf')
            for j in range(i, min(i+max_dig, n)):
                num = num*10 + int(s[j])
                if num > k: break
                min_parts = min(min_parts, num_parts(j+1))
            # print(f"{i=}, {min_parts+1}")
            return min_parts + 1
        ret = num_parts(0)
        return ret if ret != float('inf') else -1