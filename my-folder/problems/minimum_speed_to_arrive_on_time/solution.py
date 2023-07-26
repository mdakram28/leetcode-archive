class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        lo = 1
        hi = 10**7+1

        while lo < hi:
            s = (lo+hi)//2
            time_taken = sum(math.ceil(d/s) for d in dist[:-1]) + dist[-1]/s
            # print(s, time_taken)
            if time_taken <= hour:
                hi = s
            else:
                lo = s+1
        
        return lo if lo <= 10**7 else -1