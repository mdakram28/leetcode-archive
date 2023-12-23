class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        ans = -1
        for i in range(len(nums)):
            if total > nums[i]:
                ans = max(ans, total+nums[i])
            total += nums[i]
        return ans
