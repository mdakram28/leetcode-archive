class Solution:
    def findTheArrayConcVal(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i in range(n//2):
            ans += int(str(nums[i]) + str(nums[n-i-1]))
        if n%2:
            ans += nums[n//2]
        return ans