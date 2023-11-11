def sieve(m):
    prime = [True] * (m+1)
    prime[0] = False
    prime[1] = False
    for n in range(2, int(math.sqrt(m+1))+1):
        if not prime[n]:
            continue
        for comp in range(n*n, m+1, n):
            prime[comp] = False
    
    return prime

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)
        is_prime = sieve(n)
        primes = [i for i in range(1, n+1) if is_prime[i]]
        
        total = defaultdict(int)
        for i, n in enumerate(nums):
            i += 1
            g = 1
            for p in primes:
                if i == 1: break
                countp = 0
                while i%p == 0:
                    i //= p
                    countp += 1
                g *= p**(countp%2)
            total[g] += n
        
        return max(total.values())