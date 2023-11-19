class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        total = 0
        i = 0
        prev = nums[0]
        for num in nums:
            if prev != num:
                i += 1
                prev = num
            total += i
        return total