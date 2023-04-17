class Solution:
    def shipWithinDays(self, weights: List[int], target: int) -> int:
        n = len(weights)
        lo = max(weights)
        weights.append(0)
        for i in range(n):
            weights[i] += weights[i-1]
        hi = sum(weights)


        while lo < hi:
            mid = (lo+hi) // 2

            days = 0
            l = 0
            while l < n:
                days += 1
                r = n
                t = weights[l-1] + mid
                while l<r:
                    m2 = (l+r) // 2
                    if weights[m2] <= t:
                        l = m2+1
                    else:
                        r = m2
                

            if days > target:
                lo = mid + 1
            else:
                hi = mid
        
        return lo
            