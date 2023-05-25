class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:

        if k == 0:
            return 1

        P = [0] * (2*n+maxPts+1)
        P[0] = 1
        prev = 1

        for t in range(1, k):
            P[t] = prev/maxPts
            prev += P[t]
            prev -= P[t-maxPts]

        ans = 0
        for t in range(k, min(n+1, k+maxPts)):
            ans += prev/maxPts
            prev -= P[t-maxPts]
        
        return ans