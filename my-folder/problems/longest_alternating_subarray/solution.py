class Solution:
    def alternatingSubarray(self, nums: List[int]) -> int:
        ans = -1
        for i in range(len(nums)):
            count = 1
            diff = 1
            for j in range(i+1, len(nums)):
                if nums[j]-nums[j-1] == diff:
                    count += 1
                    diff = -diff
                else:
                    break
            # print(i, count)
            if count > 1:
                ans = max(ans, count)
        return ans