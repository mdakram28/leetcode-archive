class Solution:
    def punishmentNumber(self, n: int) -> int:
        
        @cache
        def can_partition(num, k):
            if num == k:
                return True
            r = 0
            mul = 1
            while num and r < k:
                dig = num%10
                num //= 10
                r = dig*mul + r
                mul *= 10
                if can_partition(num, k-r):
                    return True
            
            return False
        
        ans = 0
        for i in range(1, n+1):
            if can_partition(i*i, i):
                ans += i*i
        
        return ans