class Solution:
    def longestPalindrome(self, s: str) -> str:
        rows = [
            [True] * len(s),
            [True] * len(s),
            [True] * len(s)
        ]

        max_pal_len = 1
        max_pal_c = 0

        for n in range(len(s)):
            row = rows[n % 3]
            row_inner = rows[(n-2) % 3]
            for c in range(n, len(s)):
                if s[c] == s[c-n] and row_inner[c-1]:
                    row[c] = True
                    if max_pal_len < (n+1):
                        max_pal_len = n+1
                        max_pal_c = c
                else:
                    row[c] = False
        
        return s[max_pal_c - max_pal_len + 1 : max_pal_c + 1]
