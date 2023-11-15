class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        count = defaultdict(int)
        num_nums = len(set(nums))
        
        l = 0
        r = 0
        ans = 0
        # print(l, r)
        while r < len(nums):
            count[nums[r]] += 1
            r += 1
            while len(count) == num_nums and count[nums[l]] > 1:
                count[nums[l]] -= 1
                l += 1
            # print(l, r)
            if len(count) == num_nums:
                ans += l+1
        
        return ans