from string import ascii_lowercase
class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        cost = {}
        for c, v in zip(chars, vals):
            cost[c] = v
        
        for i in range(1, 27):
            c = chr(i-1 + ord('a'))
            if c not in cost:
                cost[c] = i
        t = 0
        min_t = 0
        max_diff = 0
        for c in s:
            t += cost[c]
            if t < min_t:
                min_t = t
            max_diff = max(max_diff, t-min_t)
        
        return max_diff