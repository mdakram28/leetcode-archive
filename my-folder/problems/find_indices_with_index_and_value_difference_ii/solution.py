class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        # sl = SortedList()
        maxval = (nums[0], 0)
        minval = (nums[0], 0)
        for i in range(indexDifference, len(nums)):
            if abs(nums[i]-maxval[0]) >= valueDifference:
                return [maxval[1], i]
            if abs(nums[i]-minval[0]) >= valueDifference:
                return [minval[1], i]
            if i-indexDifference+1 < len(nums):
                maxval = max(maxval, (nums[i-indexDifference+1], i-indexDifference+1))
                minval = min(minval, (nums[i-indexDifference+1], i-indexDifference+1))
        
        return [-1, -1]