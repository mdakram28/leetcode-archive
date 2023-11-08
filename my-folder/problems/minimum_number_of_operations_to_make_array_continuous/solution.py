from sortedcontainers import SortedList
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n, nums = len(nums), sorted(set(nums))
        return min(n-i-1 + bisect_right(nums, nums[i]-n, hi = i+1) for i in range(len(nums)))