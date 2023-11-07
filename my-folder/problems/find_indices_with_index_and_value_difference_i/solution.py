class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1):
                if i-j >= indexDifference and abs(nums[i]-nums[j]) >= valueDifference:
                    return [j, i]
        
        return [-1, -1]