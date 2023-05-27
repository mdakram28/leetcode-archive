class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        INF = float('inf')
        stoneValue.append(-INF)
        stoneValue.append(-INF)
        stoneValue.append(-INF)

        DP1 = [-INF] * (n+4)
        DP2 = [-INF] * (n+4)

        DP1[n] = 0
        DP2[n] = 0

        for i in range(n-1, -1, -1):
            total = 0
            for j in range(i+1, i+4):
                total += stoneValue[j-1]
                if total+DP2[j] > DP1[i]:
                    DP1[i] = total+DP2[j]
                    DP2[i] = DP1[j]
        
        a, b = DP1[0], DP2[0]
        if a > b:
            return "Alice"
        elif b > a:
            return "Bob"
        else:
            return "Tie"
        
                
