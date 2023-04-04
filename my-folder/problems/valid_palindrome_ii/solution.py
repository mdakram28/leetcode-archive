class Solution:
    def validPalindrome(self, s: str, skipped=False) -> bool:
        l = 0
        r = len(s)-1
        while l<r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                if skipped:
                    return False
                else:
                    return self.validPalindrome(s[l+1:r+1], True) or self.validPalindrome(s[l:r], True)
        return True