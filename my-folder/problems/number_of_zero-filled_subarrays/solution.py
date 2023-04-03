class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0
        for num in nums:
            if num == 0:
                count += 1
            elif count > 0:
                total += (count * (count+1)) // 2
                count = 0
        
        total += (count * (count+1)) // 2
        return total