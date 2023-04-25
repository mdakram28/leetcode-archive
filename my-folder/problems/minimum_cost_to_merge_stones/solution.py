class Solution:
    def mergeStones(self, stones: List[int], k: int) -> int:
        n = len(stones)
        if (n-1)%(k-1): return -1

        total = 0
        for i in range(n):
            total, stones[i] = total+stones[i], total
        stones.append(total)

        @cache
        def min_cost(l, r):
            if r-l < k: return 0

            cost = min(min_cost(l, mid) + min_cost(mid, r) for mid in range(l+1, r, k-1))
            
            if (r-l-1)%(k-1) == 0:
                cost += stones[r] - stones[l]

            return cost

        return min_cost(0, n)