class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0] + cuts + [n]

        @cache
        def func(l, r):
            if r-l <= 1: return 0
            elif r-l == 2: return cuts[r] - cuts[l]

            ans = float('inf')
            for i in range(l+1, r):
                ans = min(ans, func(l, i) + func(i, r))
            ans += cuts[r] - cuts[l]
            # print(f"{cuts[l]} -> {cuts[r]}, {ans=}")
            return ans
        
        return func(0, len(cuts)-1)