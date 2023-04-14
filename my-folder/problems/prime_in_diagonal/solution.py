class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        n = len(nums)
        max_val = max(max(nums[i][i], nums[i][n-i-1]) for i in range(n))
        
        is_prime = [True] * (max_val+1)
        is_prime[0] = False
        is_prime[1] = False
        
        # Generate primes
        for i in range(2, max_val+1):
            if not is_prime[i]:
                continue
            j = i*i
            while j <= max_val:
                is_prime[j] = False
                j += i
        
        max_prime = 0
        for i in range(n):
            if is_prime[nums[i][i]]:
                max_prime = max(max_prime, nums[i][i])
            # print(i, n-i-1)
            if is_prime[nums[i][n-i-1]]:
                max_prime = max(max_prime, nums[i][n-i-1])
                
        return max_prime