class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        for b in product('10', repeat=len(nums)):
            b = ''.join(b)
            if b not in nums: return b