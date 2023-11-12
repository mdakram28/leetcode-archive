class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            t = nums[i]-1
            # print(i, t, nums)
            if i == t:
                i += 1
            elif 0 <= t < len(nums):
                if nums[t] == nums[i]:
                    i += 1
                else:
                    nums[i], nums[t] = nums[t], nums[i]
            else:
                i += 1
        # print(nums)

        for i in range(n):
            if nums[i] != i+1:
                return i+1
        
        return n+1
