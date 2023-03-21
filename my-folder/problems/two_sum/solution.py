class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = list(map(lambda x: (x[1], x[0]), enumerate(nums)))
        nums.sort()
        l = 0
        r = len(nums)-1
        while l<r:
            total = nums[l][0]+nums[r][0]
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return [nums[l][1], nums[r][1]]
        return [0, 0]