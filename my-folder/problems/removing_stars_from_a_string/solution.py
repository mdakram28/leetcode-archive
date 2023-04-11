class Solution:
    def removeStars(self, s: str) -> str:
        
        stars = 0
        ret = []
        for c in s[::-1]:
            if c == '*':
                stars += 1
            elif stars > 0:
                stars -= 1
            else:
                ret.append(c)
        
        return ''.join(ret[::-1])