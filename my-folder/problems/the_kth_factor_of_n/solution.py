class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        mid = math.sqrt(n)
        i = 1
        rem = k
        while i < mid and rem:
            if n%i == 0:
                rem -= 1
            i += 1

        if rem == 0:
            return i-1

        if i>mid:
            i -= 1

        while i > 0 and rem:
            if n%i == 0:
                rem -= 1
            i -= 1
        
        if rem == 0:
            return n//(i+1)
        
        return -1