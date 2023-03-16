class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i1 in range(len(haystack) - len(needle) + 1):
            found = True
            for i2, c2 in enumerate(needle):
                if c2 != haystack[i1 + i2]:
                    found = False
                    break
            if found:
                return i1

        return -1
