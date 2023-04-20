class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        limit = right+1
        is_prime = [True] * limit
        is_prime[0] = is_prime[1] = False
        
        for i in range(2, math.ceil(math.sqrt(limit))):
            if not is_prime[i]: continue
            n = i*i
            while n < limit:
                is_prime[n] = False
                n += i
        
        last_pr = -float('inf')
        min_diff = float('inf')
        ans = (-1, -1)
        for num, pr in enumerate(is_prime):
            if pr and left <= num <= right:
                if num-last_pr<min_diff:
                    min_diff = num-last_pr
                    ans = (last_pr, num)
                last_pr = num
        return ans
                
            