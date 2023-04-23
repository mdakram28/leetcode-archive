class Solution:
    def numberOfArrays(self, s: str, k: int) -> int:
        nums = [int(c) for c in s]
        n = len(s)
        mod = 10**9+7

        @cache
        def num_ways(i):
            if i == n: return 1
            
            ways = 0
            num = 0

            while i<n:
                num = num*10 + nums[i]
                i += 1
                while i<n and nums[i] == 0:
                    num = num*10
                    i += 1
                
                if num > k:
                    break
                ways = (ways + num_ways(i))%mod

            return ways
        
        return num_ways(0)