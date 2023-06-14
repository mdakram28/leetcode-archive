class Solution:
    def isFascinating(self, n: int) -> bool:
        n = str(n) + str(n*2) + str(n*3)
        # print(n)
        return '0' not in n and len(set(n)) == 9 and len(n) == 9