class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            nums[i] = total
        freq = {
            0: 1
        }
        ways = 0
        for num in nums:
            if (num-k) in freq:
                ways += freq[num-k]
            freq[num] = freq.get(num, 0) + 1
        return ways