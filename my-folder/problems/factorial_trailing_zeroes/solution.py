class Solution:
    def trailingZeroes(self, n: int) -> int:
        n_10 = 0
        n_5 = 0
        # n_2 = 0
        for i in range(1, n+1):
            while i > 0 and i%10 == 0:
                n_10 += 1
                i //= 10
            while i > 0 and i%5 == 0:
                n_5 += 1
                i //= 5
            # while i > 0 and i%2 == 0:
            #     n_2 += 1
            #     i //= 2
        # print(f"{n_10=}, {n_5=}, {n_2=}")
        return n_10 + n_5
