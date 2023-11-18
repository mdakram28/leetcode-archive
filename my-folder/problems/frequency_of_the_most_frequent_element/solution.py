class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l=0
        total = 0
        ans = 0
        for r, num in enumerate(nums):
            total += num
            while num*(r-l+1) - total  > k:
                total -= nums[l]
                l += 1
            # print(l,r, total)
            ans = max(ans, r-l+1)
        return ans