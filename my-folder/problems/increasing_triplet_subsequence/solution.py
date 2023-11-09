class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        lowest = float('inf')
        minb = float('inf')

        for k, num in enumerate(nums):

            if num > minb:
                return True

            if num > lowest:
                # can be b
                minb = min(minb, num)
            
            if num < lowest:
                lowest = num

        return False