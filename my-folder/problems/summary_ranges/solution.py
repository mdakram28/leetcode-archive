class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        start = end = nums[0]
        ans = []
        i = 0
        n = len(nums)
        while i < n:
            start = nums[i]
            while (i+1) < n and nums[i]+1 == nums[i+1]:
                i += 1
            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(str(start) + "->" + str(nums[i]))
            i += 1
        return ans
