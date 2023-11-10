class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo = 1
        hi = max(piles)

        # def can_eat_all(k):
        #     return 

        while lo < hi:
            mid = (hi+lo)//2
            # print(mid)
            if all(
                x <= h 
                for x in accumulate(math.ceil(v/mid) for v in piles)
            ):
                hi = mid
            else:
                lo = mid+1
        
        return lo