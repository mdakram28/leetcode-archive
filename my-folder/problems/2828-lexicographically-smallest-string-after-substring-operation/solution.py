class Solution:
    def smallestString(self, s: str) -> str:
        start = 0
        while start < len(s) and s[start] == 'a':
            start += 1

        def apply(l, r):
            return s[:l] + ''.join((chr((ord(c)-ord('a')-1)%26 + ord('a')) for c in s[l:r])) + s[r:]

        if start == len(s):
            return apply(len(s)-1, len(s))

        pos = s.find('a', start)


        if pos == -1:
            return apply(start, len(s))
        else:
            return apply(start, pos)
