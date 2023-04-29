class Solution:
    def xorBeauty(self, nums: List[int]) -> int:
        ans = 0
        dig = 0
        lim = max(nums)
        while (mask := 1 << dig) <= lim:
            count = sum(1 for num in nums if num&mask)
            if count%2:
                ans |= 1<<dig
            
            dig += 1
        return ans