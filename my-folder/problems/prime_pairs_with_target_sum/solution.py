def sieve(num): 
    is_prime = [True] * (num+1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range(2, int(math.sqrt(num))+1):
        if is_prime[p] == False:
            continue
        for c in range(p*p, num+1, p):
            is_prime[c] = False
    return is_prime


class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        is_prime = sieve(n)
        ans = []
        for i, p in enumerate(is_prime[:n//2+1]):
            if p and is_prime[n-i]:
                ans.append((i, n-i))
        return ans