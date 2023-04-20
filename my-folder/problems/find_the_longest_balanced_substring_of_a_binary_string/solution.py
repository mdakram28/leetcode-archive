class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        n = len(s)
        i = 0
        max_bal = 0
        while i<n:
            start = i
            while i<n and s[i] == '0':
                # zeroes += 1
                i += 1
            zeroes = i-start
            start = i
            while i<n and s[i] == '1':
                # ones += 1
                i += 1
            ones = i-start
            max_bal = max(max_bal, min(zeroes, ones))
        return max_bal*2
            
            