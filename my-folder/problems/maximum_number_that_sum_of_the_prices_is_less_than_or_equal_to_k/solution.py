class Solution:
    def findMaximumNumber(self, k: int, x: int) -> int:
        def count_upto(num):
            total = 0
            for bit in range(x, 60, x):
                total += (num//(1<<bit))*(1<<(bit-1)) + max(0, num%(1<<bit)-(1<<(bit-1)))
            return total
        
        lo = 0
        hi = 10**15 + 1
        while lo < hi:
            mid = lo + (hi-lo)//2
            count = count_upto(mid+1)
            # print(mid, count)
            if count > k:
                hi = mid
            else:
                lo = mid+1
        
        return lo-1