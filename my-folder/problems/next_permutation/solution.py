class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        last_i = -1
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                last_i = i
                break
        else:
            nums.sort()
            return
        
        print(last_i)
        repl = min(filter(lambda x: x>nums[last_i], nums[last_i+1:]))
        repl_i = nums.index(repl, last_i+1)
        print(repl, repl_i)
        nums[last_i], nums[repl_i] = nums[repl_i], nums[last_i]
        nums[last_i+1:] = sorted(nums[last_i+1:])
