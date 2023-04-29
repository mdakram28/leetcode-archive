class Solution:
    def maxJump(self, nums: List[int]) -> int:
        prev = 0
        n = len(nums)

        A = 0
        prev = 0
        for i in range(1, n, 2):
            A = max(A, nums[i] - prev)
            prev = nums[i]

        prev = 0
        for i in range(2, n, 2):
            A = max(A, nums[i] - prev)
            prev = nums[i]
        
        return max(A, nums[-1] - nums[-2])