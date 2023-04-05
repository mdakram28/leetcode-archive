class Solution:
    def leftRigthDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ret = []
        
        for n in nums:
            right -= n
            ret.append(abs(left-right))
            left += n
        
        return ret
        