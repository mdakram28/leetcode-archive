class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
            return 0
        primes = [True] * n
        primes[0] = False
        primes[1] = False
        # removed = 1
        for p in range(2, n//2+1):
            if not primes[p]:
                continue
            # removed = 0
            for comp in range(p*2, n, p):
                primes[comp] = False
                # removed += 1
        return sum(1 for p in primes if p)