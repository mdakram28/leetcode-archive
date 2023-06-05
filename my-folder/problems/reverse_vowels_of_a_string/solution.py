class Solution:
    def reverseVowels(self, s: str) -> str:
        rev = []
        vow = []
        for c in s:
            if c.lower() in ('a', 'e', 'i', 'o', 'u'):
                vow.append(c)
                rev.append(None)
            else:
                rev.append(c)


        for i, v in enumerate(rev):
            if v is None:
                rev[i] = vow.pop()
        
        return ''.join(rev)