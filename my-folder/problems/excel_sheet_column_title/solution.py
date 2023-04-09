from string import ascii_uppercase
class Solution:
    def convertToTitle(self, n: int) -> str:
        ret = []
        while n:
            n-=1
            ret.append(ascii_uppercase[n%26])
            n //= 26
        
        return ''.join(ret[::-1])