class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        # stations.append([target, 0])
        dp = [startFuel]

        for i, (position, fuel) in enumerate(stations):
            dp.append(0)
            for j in range(i, -1, -1):
                if dp[j] >= position:
                    dp[j+1] = max(
                        dp[j+1],
                        dp[j] +  fuel
                    )

        for i,d in enumerate(dp):
            if d >= target:
                return i

        return -1