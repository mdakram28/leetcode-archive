class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        
        count = 1
        total = nums[0]
        for j in range(1, n):
            if nums[j] == nums[j-1]+1:
                count += 1
                total += nums[j]
            else:
                break
                
        
        # print(max_l, max_sum)
        nums = set(nums)
        for ans in itertools.count(total):
            if ans not in nums:
                return ans