class Solution:
    def knightDialer(self, n: int) -> int:
        g1 = [1]*12
        g2 = [0]*12
        g1[9] = 0
        g1[11] = 0
        if n > 1:
            g1[4] = 0
        mod = 10**9+7

        for i in range(n-1):
            g2[0] = (g1[7] + g1[5]) % mod
            g2[1] = (g1[6] + g1[8]) % mod
            g2[2] = (g1[3] + g1[7]) % mod
            g2[3] = (g1[2] + g1[8] + g1[10]) % mod
            g2[5] = (g1[0] + g1[6] + g1[10]) % mod
            g2[6] = (g1[1] + g1[5]) % mod
            g2[7] = (g1[0] + g1[2]) % mod
            g2[8] = (g1[1] + g1[3]) % mod
            g2[10] = (g1[3] + g1[5]) % mod

            g1, g2 = g2, g1
        
        return sum(g1) % mod