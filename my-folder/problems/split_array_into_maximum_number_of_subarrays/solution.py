class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        t = nums[0]
        for num in nums:
            # print(bin(num))
            t &= num
        
        if t > 0:
            return 1
        
        # print("target", bin(t))
        
        curr = 0xffffff
        total = 0
        for num in nums:
            curr &= num
            # print(num, bin(curr))
            if curr == 0:
                total += 1
                curr = 0xffffff
        
        return total