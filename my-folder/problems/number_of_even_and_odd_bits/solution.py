import math
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        l = math.floor(math.log2(n))
        even = 0
        odd = 0
        i = 0
        while i<=l and n:
            # print(l, bin(n))
            if i%2:
                if n&1:
                    # print("Found odd")
                    odd += 1
            else:
                if n&1:
                    # print("Found even")
                    even += 1
            n = n>>1
            i += 1 
        
        return [even, odd]