class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # num_pos = sum(1 if num>=0 else 0 for num in nums)
        inf = float('inf')
        # if num_pos == 0:
        #     a, b, c = -inf, -inf, -inf
        #     for num in nums:
        #         if num >= a:
        #             a, b, c = num, a, b
        #         elif num >= b:
        #             b, c = num, b
        #         elif num > c:
        #             c = num
        #         # print(a, b, c)
        #     return a*b*c
        # elif num_pos < 3:
        #     a, b = inf, inf
        #     z = -inf
        #     for num in nums:
        #         if num <= a:
        #             a, b = num, a
        #         elif num <= b:
        #             b = num
        #         if num > z:
        #             z = num
        #     return a*b*z
        # else:
        a, b = inf, inf
        x, y, z = -inf, -inf, -inf
        for num in nums:
            if num <= a:
                a, b, c = num, a, b
            elif num <= b:
                b, c = num, b
            elif num < c:
                c = num

            if num >= x:
                x, y, z = num, x, y
            elif num >= y:
                y, z = num, y
            elif num > z:
                z = num
        return max(a*b*x, x*y*z)
