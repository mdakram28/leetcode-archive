from sortedcontainers import SortedList
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        nums.sort()
        l = 0
        r = len(nums)-1
        ans = 0
        while l<r:
            while r > l and nums[r] >= target-nums[l]:
                r -= 1
            # print(l, r)
            ans += r-l
            l += 1
        return ans