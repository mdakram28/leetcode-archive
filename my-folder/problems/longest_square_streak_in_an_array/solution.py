class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        ans = -1
        nums.sort()
        rem = set(nums)
        for num in nums:
            l = 0
            while num in rem:
                rem.remove(num)
                num = num*num
                l += 1
            if l >= 2: ans = max(ans, l)
        return ans
                