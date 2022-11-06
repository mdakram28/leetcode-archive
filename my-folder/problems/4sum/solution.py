class Solution:
    def twosum(self, nums, l, r, target):
        while l<r:
            total = nums[l] + nums[r]
            if total == target:
                yield [nums[l],nums[r]]
            if total < target:
                l += 1
                while l<r and nums[l] == nums[l-1]:
                    l += 1
            else:
                r -= 1
                while l<r and nums[r] == nums[r+1]:
                    r -= 1
        
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        ret = []
        nums.sort()
        l = len(nums)
        
        i = 0
        while i < l-3:
            j = i+1
            while j < l-2:
                for ts in self.twosum(nums, j+1, l-1, target-nums[i]-nums[j]):
                    ret.append([nums[i], nums[j], ts[0], ts[1]])
                j += 1
                while j<l-2 and nums[j] == nums[j-1]:
                    j += 1
            i += 1
            while i<l-3 and nums[i] == nums[i-1]:
                i += 1
        return ret
            


# sol = Solution()
# print(sol.fourSum([-3,-2,-1,0,0,1,2,3], 0))