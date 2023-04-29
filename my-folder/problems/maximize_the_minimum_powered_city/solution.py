class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        # print(f"--------------------- {stations=}, {r=}, {k=}")
        n = len(stations)
        A = [0] * n
        for i, s in enumerate(stations):
            A[max(i-r, 0)] += s
            if i+r+1 < n:
                A[i+r+1] -= s
        total = 0
        for i, d in enumerate(A):
            total += d
            A[i] = total
        # print(A)
        
        B = defaultdict(int)
    
        def stations_required(min_power):
            B.clear()
            diff = 0
            ans = 0
            for i, power in enumerate(A):
                diff += B[i]
                req = min_power - (power+diff)
                if req > 0:
                    B[i + 2*r + 1] -= req
                    diff += req
                    ans += req
            return ans
        
        if k == 0:
            return min(A)
        
        lo = 0
        hi = max(A) + k + 1
        while lo < hi:
            mid = (lo+hi)//2
            req = stations_required(mid)
            # print(mid, req, B)
            if req <= k:
                lo = mid+1
            else:
                hi = mid
        
        return lo-1
                    
                    
                    