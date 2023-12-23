class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        
        count = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                arr = nums[:i] + nums[j+1:]
                if all(arr[i] > arr[i-1] for i in range(1, len(arr))):
                    count += 1
        
        return count
