class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        bits = 0xFFFFFFFFFF
        for num in nums:
            if num&(num-1) == 0:
                bits &= ~num
        # print(bin(bits))
        n = 1
        while True:
            if bits&n:
                return n
            n <<= 1