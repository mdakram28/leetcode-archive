class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = [0] * 128
        for c in s:
            freq[ord(c)] += 1
        
        pairs = 0
        for c in range(ord('a'), ord('z')+1):
            pairs += freq[c] // 2
        for c in range(ord('A'), ord('Z')+1):
            pairs += freq[c] // 2
        # print(pairs)
        if pairs*2 < len(s):
            return pairs*2 + 1
        else:
            return pairs*2