class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        total = nums[0]
        nums[0] = float('inf')
        heapify(nums)
        total += heappop(nums) + heappop(nums)
        return total