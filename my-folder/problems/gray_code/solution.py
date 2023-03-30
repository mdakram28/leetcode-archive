class Solution:
    def grayCode(self, n: int) -> List[int]:
        nums = [0, 1]

        for d in range(1, n):
            a = 1<<d
            for i in range(len(nums)-1, -1, -1):
                nums.append(a+nums[i])
        
        return nums