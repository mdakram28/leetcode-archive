class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        count = 0
        for num in nums:
            if num%2 == 0:
                count += 1
                if count == 2:
                    return True
        
        return False
        