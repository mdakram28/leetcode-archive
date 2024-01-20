class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        n = len(nums)
        setBits = [bin(num).count("1") for num in nums]
        
        nums.append(float('inf'))
        setBits.append(100000)
        
        l = 0
        for i in range(1, n+1):
            if (setBits[i] != setBits[i-1]):
                nums[l:i] = sorted(nums[l:i])
                l = i
        
        for i in range(1, n+1):
            if nums[i] < nums[i-1]:
                return False
        
        return True