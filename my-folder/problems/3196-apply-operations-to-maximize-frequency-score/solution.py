class Solution:
    def maxFrequencyScore(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        PS = list(accumulate(nums)) + [0]

        def get_cost(l, r):
            mid = (l+r)//2
            return nums[mid]*(mid-l+1) - (PS[mid]-PS[l-1]) + (PS[r]-PS[mid-1]) - nums[mid]*(r-mid+1)

        l = 0
        ans = 0
        for r in range(n):
            while get_cost(l, r) > k:
                l += 1
            ans = max(ans, r-l+1)

        return ans
