class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cum_sum = nums[0]
        curr_min = min(0, nums[0])
        
        max_diff = nums[0]

        for i in range(1, len(nums)):
            cum_sum += nums[i]
            max_diff = max(max_diff, cum_sum - curr_min)
            if cum_sum < curr_min:
                curr_min = cum_sum
            
            # print(f"{i=}, {cum_sum=}, {curr_min=}, {max_diff=}")
        
        return max_diff
