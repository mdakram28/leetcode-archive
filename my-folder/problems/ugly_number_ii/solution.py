class Solution:

    def nthUglyNumber(self, n: int) -> int:
        uglies = [0] * n
        uglies[0] = 1
        ia, ib, ic = 0, 0, 0
        a, b, c = 2, 3, 5

        for i in range(1, n):
            uglies[i] = u = min(a, b, c)
            if a == u:
                ia += 1
                a = uglies[ia]*2
            if b == u:
                ib += 1
                b = uglies[ib]*3
            if c == u:
                ic += 1
                c = uglies[ic]*5

        return uglies[-1]