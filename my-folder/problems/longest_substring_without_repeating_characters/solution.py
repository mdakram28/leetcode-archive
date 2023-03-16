class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_i = {}
        start = -1
        max_diff = 0
        for i, c in enumerate(s):
            if c in last_i:
                start = max(last_i[c], start)
            last_i[c] = i
            max_diff = max(max_diff, i - start)
        return max_diff
        