class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        seq = []
 
        for num in nums:
            d = collections.defaultdict(int)
            for i in range(len(seq)):
                d[nums[i]-num] = seq[i][nums[i]-num] + 1
            seq.append(d)
        
        return max(max(d.values()) for d in seq) + 1