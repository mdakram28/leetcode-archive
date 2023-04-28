class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            if num < 10: continue
            mul = 1
            while num:
                total += (num%10)*mul - num%10
                num //= 10
                mul *= 10
        
        return total