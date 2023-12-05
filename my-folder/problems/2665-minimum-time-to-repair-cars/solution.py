class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        count = Counter(ranks)
        ranks = list(count.keys())
        ranks.sort()


        def can_repair_in_time(t):
            rem = cars
            for r in ranks:
                n = isqrt(t//r)*count[r]
                rem -= n
                if rem <= 0:
                    return True
            
            return False
        
        lo = 0
        hi = ranks[0]*(math.ceil(cars/count[ranks[0]])**2)

        while lo < hi:
            mid = lo + (hi-lo)//2
            if can_repair_in_time(mid):
                hi = mid
            else:
                lo = mid+1
        
        return lo

