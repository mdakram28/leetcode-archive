class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_pos = 0
        for i,jump in enumerate(nums):
            if i>max_pos:
                return False
            max_pos = max(max_pos, i+jump)
        return True