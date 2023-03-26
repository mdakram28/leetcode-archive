class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return  nums[0]

        m1_prev = nums[0]
        m1_curr = max(nums[0], nums[1])

        m2_prev = 0
        m2_curr = nums[1]

        for num in nums[2:-1]:
            m1_prev, m1_curr = m1_curr, max(num + m1_prev, m1_curr)
            m2_prev, m2_curr = m2_curr, max(num + m2_prev, m2_curr)
        
        
        return max(m2_prev + nums[-1], m1_curr)