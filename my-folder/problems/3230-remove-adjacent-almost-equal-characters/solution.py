class Solution:
    def removeAlmostEqualCharacters(self, word: str) -> int:
        
        ans = 0
        count = 1
        for i in range(1, len(word)):
            if abs(ord(word[i])-ord(word[i-1])) <= 1:
                count += 1
            else:
                ans += count//2
                count = 1
        
        ans += count//2
        return ans
