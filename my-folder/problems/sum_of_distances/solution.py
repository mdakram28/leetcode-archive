class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        loc_sum = collections.defaultdict(int)
        freq = collections.defaultdict(int)
        
        ret = [0] * len(nums)
        for i in range(len(nums)):
            if freq[nums[i]]:
                ret[i] = i*freq[nums[i]] - loc_sum[nums[i]]
            loc_sum[nums[i]] += i
            freq[nums[i]] += 1
        
        freq.clear()
        loc_sum.clear()
        for i in range(len(nums)-1, -1, -1):
            if freq[nums[i]]:
                ret[i] += loc_sum[nums[i]] - i*freq[nums[i]]
            loc_sum[nums[i]] += i
            freq[nums[i]] += 1
        
        return ret