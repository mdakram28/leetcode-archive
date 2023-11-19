class Solution:
    def minimumSteps(self, s: str) -> int:
        i = 0
        total = 0
        for j,c in enumerate(s):
            if c == '0':
                total += j-i
                i += 1
        return total