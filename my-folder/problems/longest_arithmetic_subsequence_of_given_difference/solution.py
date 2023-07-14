class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp_len = defaultdict(int)

        for num in arr:
            dp_len[num] = max(dp_len[num], dp_len[num-difference] + 1)
        
        return max(dp_len.values())