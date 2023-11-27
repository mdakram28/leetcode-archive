class Solution:
    def isFascinating(self, n: int) -> bool:
        num = str(n)+str(2*n)+str(3*n)
        # print(num)
        return "0" not in num and len(set(num)) == 9 and len(num) == 9
