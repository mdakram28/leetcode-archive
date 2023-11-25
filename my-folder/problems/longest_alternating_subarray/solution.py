class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            count = 1
            diff = 1
            for j in range(i+1, len(nums)):
                if nums[j] - nums[j-1] != diff:
                    break
                diff = -diff
                count += 1
            if count > 1:
                ans = max(ans, count)
        
        return ans