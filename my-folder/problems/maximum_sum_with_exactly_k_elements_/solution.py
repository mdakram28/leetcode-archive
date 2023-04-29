class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        return (k*(k-1))//2 + max(nums)*k