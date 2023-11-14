class Solution:
    def minOperations(self, nums: List[int]) -> int:
        a = 0
        b = 0
        for num in nums:
            if num == 0: continue
            binary = bin(num)
            # print(binary, binary.count("1"), len(binary)-3)
            a += binary.count("1")
            b = max(b, len(binary)-3)
        return a + b