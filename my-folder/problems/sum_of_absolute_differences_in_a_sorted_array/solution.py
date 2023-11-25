class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        right = sum(nums)
        left = 0
        result = [0]*len(nums)

        for i, num in enumerate(nums):
            right -= num
            result[i] = (i*num - left) + (right - (len(nums)-i-1)*num)
            left += num

        return result