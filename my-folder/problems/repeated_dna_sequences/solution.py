class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:

        def encode_char(s: str) -> int:
            '''
            Return binary for a character
            '''
            if s == 'A':
                return 0b00
            elif s == 'C':
                return 0b01
            elif s == 'G':
                return 0b10
            else:
                return 0b11

        end = 0
        start = 0
        l = len(s)
        n = 0b0
        d = {}
        limits = {}

        if l <= 10:
            return []

        while end < 10:
            b = encode_char(s[end])
            n = (n << 2) | b
            end += 1
        
        d[n] = 1

        while end < l:
            b = encode_char(s[end])
            n = ((n << 2) | b) & 0b11111111111111111111
            end += 1
            start += 1
            d[n] = d.get(n, 0) + 1
            if d[n] == 2:
                limits[n] = (start, end)
        
        ret = []
        for start, end in limits.values():
            ret.append(s[start:end])

        return ret



