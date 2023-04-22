class Solution:
    def minOperations(self, n: int) -> int:
        op = 0
        while n:
            while n&1 == 0:
                n >>= 1
            # print(bin(n))
            op += 1
            if n&0b10:
                n += 1
            else:
                n -= 1
                # if n == 0: break
            
        return op