class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        start = 0
        count = 0
        VOWELS = 'aeiou'
        ans = 0
        for end in range(len(s)+1):
            while end-start > k:
                if s[start] in VOWELS:
                    count -= 1
                start += 1
            
            # print(start, end, count)
            ans = max(ans, count)

            if end < len(s) and s[end] in VOWELS:
                count += 1
        
        return ans