class Solution:
    @cache
    def isScramble(self, s1: str, s2: str) -> bool:
        # print(f"{s1=}, {s2=}")
        l = len(s1)
        if l == 1 and s1[0] == s2[0]:
            return True
        nz = 0<<26
        freq = [0] * 26
        for i in range(len(s1)-1):
            c1 = ord(s1[i]) - 97
            c2 = ord(s2[l-i-1]) - 97
            if c1 != c2:
                freq[c1] += 1
                freq[c2] -= 1
                if freq[c1]:
                    nz |= 1<<c1
                else:
                    nz &= ~(1<<c1)
                if freq[c2]:
                    nz |= 1<<c2
                else:
                    nz &= ~(1<<c2)
            # print(f"{i=}, {bin(nz)}")
            if nz == 0 and (
                self.isScramble(s1[:i+1], s2[l-i-1:]) and 
                self.isScramble(s1[i+1:], s2[:l-i-1])
                ):
                return True
        nz = 0<<26
        freq = [0] * 26
        # print("-----------------")
        for i in range(len(s1)-1):
            c1 = ord(s1[i]) - 97
            c2 = ord(s2[i]) - 97
            if c1 != c2:
                freq[c1] += 1
                freq[c2] -= 1
                if freq[c1]:
                    # print(f"{c1} became non-zero")
                    nz |= 1<<c1
                else:
                    nz &= ~(1<<c1)
                if freq[c2]:
                    # print(f"{c2} became non-zero")
                    nz |= 1<<c2
                else:
                    nz &= ~(1<<c2)
            # print(f"{i=}, {c1=}, {c2=}, {bin(nz)}")
            if nz == 0 and (
                self.isScramble(s1[:i+1], s2[:i+1]) and 
                self.isScramble(s1[i+1:], s2[i+1:])
                ):
                return True
        
        return False
                
        