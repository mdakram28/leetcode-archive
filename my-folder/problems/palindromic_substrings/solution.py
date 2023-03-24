class Solution:
    def countSubstrings(self, s: str) -> int:
        pal = [True for i in range(len(s))]
        count = 0
        for i in range(len(s)):
            for j in range(i):
                pal[j] = s[i] == s[j] and pal[j+1]
                if pal[j]:
                    count += 1
            count += 1
        
        return count