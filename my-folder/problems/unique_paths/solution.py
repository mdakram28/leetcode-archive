class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        l = [1 for i in range(n)]

        for _ in range(1, m):
            t = 1
            for j in range(1, n):
                t += l[j]
                l[j] = t
            # print(l)
        
        return l[-1]