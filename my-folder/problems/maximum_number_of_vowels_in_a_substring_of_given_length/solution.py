class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        count = 0
        VOWELS = ('a', 'e', 'i', 'o', 'u')
        for i in range(k-1):
            if s[i] in VOWELS:
                count += 1
        ans = count
        for i in range(k-1, len(s)):
            if s[i] in VOWELS:
                count += 1
            ans = max(ans, count)
            if s[i-k+1] in VOWELS:
                count -= 1

        return ans