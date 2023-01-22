class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        # print(nums)
        min_total = 0
        min_diff = float('inf')
        for first in range(len(nums)-2):
            t = target - nums[first]

            i = first+1
            j = len(nums)-1
            closest = (i,j)
            closest_diff = abs(nums[i]+nums[j]-t)
            while (j-i) > 1:
                if (nums[i] + nums[j]) < t:
                    i += 1
                elif (nums[i] + nums[j]) > t:
                    j -= 1
                else:
                    closest = (i,j)
                    break
                diff = abs(nums[i] + nums[j] - t)
                if diff < closest_diff:
                    closest_diff = diff
                    closest = (i,j)
            # print(f'{nums[first]=}, {t=}, {nums[closest[0]]=}, {nums[closest[1]]=}')
            total = nums[first] + nums[closest[0]] + nums[closest[1]]
            diff = abs(total - target)
            if diff < min_diff:
                min_diff = diff
                min_total = total
        return min_total

