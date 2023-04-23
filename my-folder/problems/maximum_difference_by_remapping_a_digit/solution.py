class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = list(str(num))
        min_val = int(''.join('0' if n == nums[0] else n for n in nums))
        
        non9 = 0
        for i in range(len(nums)):
            if nums[i] != '9':
                non9 = i
                break
        else:
            return num
        max_val = int(''.join('9' if n == nums[non9] else n for n in nums))
        return max_val - min_val