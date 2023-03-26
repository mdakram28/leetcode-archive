class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        num = 0
        for c in columnTitle:
            num = num*26 + (ord(c) - ord('A') + 1)
        return num