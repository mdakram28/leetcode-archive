class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []

        def add_subsets(i, pref):
            if i == len(nums):
                ret.append([*pref])
                return
            count = 1
            while (i+count) < len(nums) and nums[i+count] == nums[i]:
                count += 1
            
            add_subsets(i+count, pref)
            for j in range(i, i+count):
                pref.append(nums[i])
                add_subsets(i+count, pref)
            
            for j in range(count):
                pref.pop()

        add_subsets(0, [])

        return ret