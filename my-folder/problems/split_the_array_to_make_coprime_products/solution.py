mx = 10**6
spf = [i for i in range(mx+1)]
for i in range(2,int(math.sqrt(mx))+1):
    if spf[i]==i:
        for j in range(i*i,mx+1,i):
            spf[j]=min(spf[j],i)
def getPrimeFactors(x):
    while x!=1:
        yield spf[x]
        x//=spf[x]

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        # def get_pfactors(num):
        #     # print(f"get_pfactors({num})")
        #     ret = []
        #     for prime in primes:
        #         if num%prime == 0:
        #             # print(f"{num=}, {prime=}, {num_div=}")
        #             while num%prime == 0:
        #                 num //= prime
        #             ret.append(prime)
        #     return ret
        
        # is_prime = [True] * 1000005
        # is_prime[1] = False
        # primes = []
        # for p in range(2, 1000005):
        #     if not is_prime[p]:
        #         continue
        #     primes.append(p)
        #     j = p*p
        #     while j < 1000005:
        #         is_prime[j] = False
        #         j += p
        
        # pfactors = list(map(getPrimeFactors, nums))
        # print(pfactors)
        
        last_idx = {}
        for i in range(len(nums)):
            for p in getPrimeFactors(nums[i]):
                last_idx[p] = i
        
        end = 0
        i = 0
        while i <= end:
            for p in getPrimeFactors(nums[i]):
                end = max(end, last_idx[p])
            i += 1
        
        return end if end < (len(nums)-1) else -1
        
        
        
        
        