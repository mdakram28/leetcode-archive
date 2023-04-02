class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        primes = [True] * 1005
        primes[0] = False
        primes[1] = False
        for n in range(2, len(primes)):
            if not primes[n]:
                continue
            j = n*n
            while j < 1005:
                primes[j] = False
                j += n
        
        # print(primes[:20])
        
        prev = 0
        for n in nums:
            for n2 in range(n-prev-1, 1, -1):
                if not primes[n2]:
                    continue
                # primes[n2] = False
                # print(f"{n=}, {n2=}")
                n -= n2
                break
            else:
                if n <= prev:
                    return False
            # print(n)
            prev = n
        
        return True