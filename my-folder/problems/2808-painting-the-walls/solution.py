class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)

        # Diff can go from -n to +n
        DP = [0]*(n+1) + [float('inf')]*n
        DP2 = [0]*(2*n+1)
        for i in range(n):
            for d in range(-(n-i), n+1):
                if d >= (i+1):
                    DP2[d] = 0
                else:
                    DP2[d] = min(
                        cost[i]+(DP[d+time[i]] if (d+time[i]) <= n else 0),
                        DP[d-1]
                    )
            DP, DP2 = DP2, DP
        
        return DP[0]
