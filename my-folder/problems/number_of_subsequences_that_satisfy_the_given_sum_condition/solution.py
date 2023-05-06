from sortedcontainers import SortedList

class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums = SortedList(nums)
        ans = 0
        mod = 10**9 + 7
        for i in range(nums.bisect_right(target//2)):
            t = target-nums[i]
            r = nums.bisect_right(t)
            # print(num, i, r)
            ans = (ans + pow(2, r-i-1, mod)) % mod
        
        return ans


