class Solution:
    def distinctAverages(self, nums: List[int]) -> int:
        nums.sort()
        avg = set()
        for a,b in zip(nums[:len(nums)//2], nums[len(nums)//2:][::-1]):
            avg.add(a+b)
        return len(avg)