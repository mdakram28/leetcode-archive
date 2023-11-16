class Solution:
    def maxArrayValue(self, nums: List[int]) -> int:
        
        ans = 0
        while len(nums)>1:
            if nums[-1] >= nums[-2]:
                nums.append(nums.pop()+nums.pop())
            else:
                ans = max(ans, nums.pop())
        ans = max(ans, nums.pop())
        return ans