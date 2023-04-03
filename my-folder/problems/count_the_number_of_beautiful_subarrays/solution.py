class Solution:
    def beautifulSubarrays(self, nums: List[int]) -> int:
        xor = 0
        i = 0
        while i < len(nums):
            xor ^= nums[i]
            nums[i] = xor
            i += 1
        # print(list(map(bin, nums)))
        total = 0
        freq = collections.defaultdict(int)
        freq[0] = 1
        for num in nums:
            total += freq[num]
            freq[num] += 1
        
        return total