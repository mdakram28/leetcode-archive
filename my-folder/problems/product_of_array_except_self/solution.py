class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        suff = []
        for num in nums[::-1]:
            suff.append(prod)
            prod *= num
        suff.reverse()

        prod = 1
        for i, num in enumerate(nums):
            suff[i] *= prod
            prod *= num
        
        return suff